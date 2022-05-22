import logging
import os

from flask import Flask, make_response, render_template, request
from flask_restful import Api
from flask_cors import CORS

import db
from PlayerProfile import PlayerProfile, PlayerProfileList

app = Flask(__name__)
api = Api(app)

# TODO restrict resources to front-end container, once it exists
CORS(app)

logging.basicConfig(level=os.environ.get('LOGLEVEL', 'INFO'))
log = logging.getLogger(__name__)

# landing page
@app.route('/', methods=['GET'])
def landing_page():
  return "It's a landing page, alright."

api.add_resource(PlayerProfileList, '/playerProfiles')
api.add_resource(PlayerProfile, '/playerProfiles/<int:player_profile_id>')

# nuke all DB entries
@app.route('/resetDB')
def reset_db():
  return db.reset()

if __name__ == '__main__':
    app.run(debug=True)
