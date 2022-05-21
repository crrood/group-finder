import os
from pymongo import MongoClient

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
  return 'db reset'