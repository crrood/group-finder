import logging
from bson import json_util, ObjectId
from flask import make_response, request
from flask_restful import Resource

from utils.validator import Auth0Wrapper
import utils.db as db

auth = Auth0Wrapper()
log = logging.getLogger(__name__)

class PlayerCharacter(Resource):
  # NOTE authentication is disabled for testing
  # @auth.require_auth(None)
  def get(self, player_character_id):
    collection = db.get_collection('playerCharacters')
    try:
      object_id = db.convert_to_oid(player_character_id)
    except:
      return f'Could not convert {player_character_id} to ObjectId', 422

    data = collection.find_one({'_id': object_id})

    if data != None:
      log.info(json_util.dumps(data))
      return json_util.dumps(data), 200
    else:
      return f'playerCharacter with id {player_character_id} not found', 404
  
  # NOTE authentication is disabled for testing
  # @auth.require_auth(None)
  def put(self, player_character_id):
    player_character = request.get_json()
    
    # remove immutable _id from incoming data
    player_character.pop('_id', None)

    # convert id to ObjectId
    try:
      object_id = db.convert_to_oid(player_character_id)
    except:
      return f'Could not convert {player_character_id} to ObjectId', 422
    
    client = db.get_collection('playerCharacters')
    result = client.replace_one(
        {'_id': object_id}, player_character, upsert=True)

    if result.matched_count > 0:
      response = 'updated'
    elif result.upserted_id != None:
      response = 'inserted'
    else:
      response = 'something weird happened...'
    return response, 200

class PlayerCharacterList(Resource):
  def get(self):
    # return all documents from PlayerCharacters collection
    player_characters_collection = db.get_collection('playerCharacters')

    results = player_characters_collection.find()
    result_string = ''
    for result in results:
      result_string = result_string + json_util.dumps(result) + '<hr>'

    return make_response(result_string, 200)
