import logging
import os

import utils.db as db
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from models.PlayerCharacter import PlayerCharacter, PlayerCharacterList
from models.User import User, UserList
from utils.validator import Auth0Wrapper

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False
api = Api(app)
auth = Auth0Wrapper()

# TODO restrict resources to front-end container, once it exists
CORS(app)

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))


# landing page
@app.route("/", methods=["GET"])
def landing_page():
    return "It's a landing page, alright."


api.add_resource(PlayerCharacterList, "/playerCharacters")
api.add_resource(PlayerCharacter, "/playerCharacters/<string:player_character_id>")
api.add_resource(UserList, "/users")
api.add_resource(User, "/users/<string:user_id>")


# nuke all DB entries
@app.route("/resetDB")
def reset_db():
    logging.warn("resetting DB")
    return db.reset()


if __name__ == "__main__":
    app.run(debug=True)
