from bson import json_util
from flask import make_response
from flask_restful import Resource

import db


class PlayerProfile(Resource):
  def get(self, player_profile_id):
    data = {
      'id': player_profile_id,
      'name': 'Thumper Strongbottom Jr',
      'thumbnail': 'https://i.pinimg.com/originals/7b/f4/ae/7bf4ae7ccd11422ccb2a8b4017198b65.png'
    }
    return data
  
  def patch(self, player_profile_id):
    player_profile = {"id": player_profile_id}
    client = db.get_collection('playerProfiles')
    client.insert_one(player_profile)
    return "done", 201

class PlayerProfileList(Resource):
  def get(self):
    # return all documents from PlayerProfiles collection
    player_profiles_collection = db.get_collection('playerProfiles')

    results = player_profiles_collection.find()
    result_string = ''
    for result in results:
      result_string = result_string + json_util.dumps(result) + '<hr>'

    return make_response(result_string, 200)
