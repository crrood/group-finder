import logging
from flask import request
from flask_restful import Resource
from bson.objectid import ObjectId

from utils.validator import Auth0Wrapper
import utils.db as db

auth = Auth0Wrapper()

class User(Resource):
  def get(self, user_id):
    return db.get_document_by_id('users', user_id)

  def put(self, user_id):
    data = request.get_json()
    return db.upsert_document('users', data, {'auth0Id': user_id})

class UserList(Resource):
  def get(self):
    return db.query_collection('users')
