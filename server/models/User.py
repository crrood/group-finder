import logging
from flask import make_response, request
from flask_restful import Resource

from utils.validator import Auth0Wrapper
import utils.db as db

auth = Auth0Wrapper()

class UserProfile(Resource):
  def get(self, user_id):
    return db.get_document_by_id('users', user_id)

  def put(self, user_id):
    return db.upsert_document('users', user_id, request.get_json())