import json
import os
from pymongo import MongoClient
from bson import ObjectId

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

# drop the DB
def reset():
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