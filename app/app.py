import logging
import os

from bson import json_util
from flask import Flask, make_response, render_template, request
from flask_restful import Api, Resource

import db

app = Flask(__name__)
api = Api(app)

logging.basicConfig(level=os.environ.get('LOGLEVEL', 'INFO'))
log = logging.getLogger(__name__)

# landing page
@app.route('/', methods=['GET'])
def landing_page():
  return render_template('landing_page.html')

class PlayerProfile(Resource):
  def get(self, player_profile_id):
    return {'id': player_profile_id}
  
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

api.add_resource(PlayerProfileList, '/playerProfiles')
api.add_resource(PlayerProfile, '/playerProfiles/<int:player_profile_id>')

# nuke all DB entries
@app.route('/resetDB')
def reset_db():
  return db.reset()

if __name__ == '__main__':
    app.run(debug=True)
