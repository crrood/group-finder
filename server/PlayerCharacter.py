from bson import json_util
from flask import make_response
from flask_restful import Resource

from validator import Auth0Wrapper
import db

auth = Auth0Wrapper()

SAMPLE_DATA = {
  "id": 0,
  "userId": 0,
  "photo": {
    "id": 0,
    "fullsize": "https://i.pinimg.com/originals/7b/f4/ae/7bf4ae7ccd11422ccb2a8b4017198b65.png",
    "thumbnail": "https://placekitten.com/100/100"
  },
  "answers": [
    {
      "id": 0,
      "text": "I would never consider such a thing!",
      "playerProfileId": 0,
      "question": {}
    }
  ],
  "name": "Thumper Strongbottom",
  "race": "Halfing",
  "gender": "Male",
  "height": "3ft 7in",
  "weight": "8 stone",
  "background": "Farmer",
  "description": "A folksy little man with a dark side",
  "personalityTraits": "Has an earthy wisdom, until his un-eartly patron comes out",
  "ideals": "A simple life is best",
  "bonds": "His land and family",
  "flaws": "Ignorant to the ways of the world",
  "allies": "His fellow townspeople",
  "enemies": "Gophers",
  "likes": "Carrots, onions, eternal darkness",
  "dislikes": "Poorly tilled soil",
  "catchPhrases": "Well ain't that a turnip and a half!",
  "religion": "The eternal dark one"
}

class PlayerCharacter(Resource):
  # NOTE authentication is disabled for testing
  # @auth.require_auth(None)
  def get(self, player_character_id):
    data = SAMPLE_DATA
    return data
  
  # NOTE authentication is disabled for testing
  # @auth.require_auth(None)
  def patch(self, player_character_id):
    player_character = {"id": player_character_id}
    client = db.get_collection('playerCharacters')
    client.insert_one(player_character)
    return "done", 201

class PlayerCharacterList(Resource):
  def get(self):
    # return all documents from PlayerCharacters collection
    player_characters_collection = db.get_collection('playerCharacters')

    results = player_characters_collection.find()
    result_string = ''
    for result in results:
      result_string = result_string + json_util.dumps(result) + '<hr>'

    return make_response(result_string, 200)
