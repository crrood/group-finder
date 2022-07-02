import logging
from bson import json_util
from flask import request
from flask_restful import Resource

from utils.validator import Auth0Wrapper
import utils.db as db

auth = Auth0Wrapper()

class PlayerCharacter(Resource):
  # NOTE authentication is disabled for testing
  # @auth.require_auth(None)
  def get(self, player_character_id):
    return db.get_document_by_id('playerCharacters', player_character_id)
  
  # NOTE authentication is disabled for testing
  # @auth.require_auth(None)
  def put(self, player_character_id):
    return db.upsert_document('playerCharacters', player_character_id, request.get_json())

class PlayerCharacterList(Resource):
  def get(self):
    """Return all documents from PlayerCharacters collection"""
    # TODO paginate
    player_characters_collection = db.get_collection('playerCharacters')

    results = player_characters_collection.find()
    result_string = ''
    for result in results:
      result_string = result_string + json_util.dumps(result) + '<hr>'

    return result_string, 200
