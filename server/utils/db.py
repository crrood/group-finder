import json
import logging
import os
from pymongo import MongoClient
from bson import json_util, ObjectId

DATABASE = 'groupFinder'

# connect to DB
def get_client():
  mongodb_username = os.environ.get('MONGO_INITDB_ROOT_USERNAME')
  mongodb_password = os.environ.get('MONGO_INITDB_ROOT_PASSWORD')
  mongodb_connstring = f'mongodb://{mongodb_username}:{mongodb_password}@mongodb'
  client = MongoClient(mongodb_connstring)
  return client

def get_database():
  client = get_client()
  return client[DATABASE]

def get_collection(collection):
  client = get_database()
  return client[collection]

def get_document_by_id(collection, id):
  """Query a document from the database using an _id value
  
  Parameters:
  collection (string): Name of the db collection
  id (string): ObjectID of the document

  Returns:
  (string, int): JSON dump of document OR error string, HTTP result code
  """
  client = get_collection(collection)
  try:
    object_id = convert_to_oid(id)
  except:
    response = f'Could not convert {id} to ObjectId'
    result_code = 422
    return response, result_code

  data = client.find_one({'_id': object_id})

  if data != None:
    logging.info(json_util.dumps(data))
    response = json_util.dumps(data)
    result_code = 200
  else:
    response = f'id {id} not found in {collection}'
    result_code = 404
  
  return response, result_code

def upsert_document(collection, id, data):
  """Upsert a document in the database

  Parameters:
  collection (string): Name of the db collection
  id (string): ObjectID of the document
  data (dict): JSON document to be upserted

  Returns:
  (string, int): Response message, HTTP result code
  """
  # mongo throws an error if incoming data attempts to update the immutable _id field
  data.pop('_id', None)

  try:
    object_id = convert_to_oid(id)
  except:
    response = f'Could not convert {id} to ObjectId'
    result_code = 422
    return response, result_code

  client = get_collection(collection)
  result = client.replace_one(
      {'_id': object_id}, data, upsert=True)

  if result.matched_count > 0:
    response = 'updated'
    result_code = 200
  elif result.upserted_id != None:
    response = 'inserted'
    result_code = 200
  else:
    response = 'something weird happened...'
    result_code = 202
  
  return response, result_code

def reset():
  """Drop the DB and refill with test data"""
  client = get_client()
  client.drop_database(DATABASE)
  
  # populate testing data
  with open('utils/testData/playerCharacter.json') as f:
    sample_pc_data = json.load(f)

  client = get_database()
  result = client['playerCharacters'].insert_one(sample_pc_data)

  return f'db reset - test PC id = {result.inserted_id}'

# utility methods
def convert_to_oid(id):
  return ObjectId(id)