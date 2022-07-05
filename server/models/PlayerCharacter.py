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
    return db.upsert_document_by_id('playerCharacters', request.get_json(), 
      {'_id': player_character_id})

class PlayerCharacterList(Resource):
  def get(self):
    args = request.args
    page_number = args.get("page", default=0, type=int)
    
    return db.query_collection('playerCharacters', page_number)
