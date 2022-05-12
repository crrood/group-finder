import os
from pymongo import MongoClient

DATABASE = 'groupFinder'

# connect to DB
def get_client():
  mongodb_username = open(
      os.environ['MONGO_INITDB_ROOT_USERNAME_FILE'], "r").read()
  mongodb_password = open(
      os.environ['MONGO_INITDB_ROOT_PASSWORD_FILE'], "r").read()
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