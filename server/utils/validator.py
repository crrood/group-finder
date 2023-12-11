# source: https://auth0.com/docs/quickstart/backend/python/interactive

import json
from urllib.request import urlopen

from authlib.integrations.flask_oauth2 import ResourceProtector
from authlib.jose.rfc7517.jwk import JsonWebKey
from authlib.oauth2.rfc7523 import JWTBearerTokenValidator


class Auth0JWTBearerTokenValidator(JWTBearerTokenValidator):
    def __init__(self, domain, audience):
        issuer = f"https://{domain}/"
        jsonurl = urlopen(f"{issuer}.well-known/jwks.json")
        public_key = JsonWebKey.import_key_set(json.loads(jsonurl.read()))
        super(Auth0JWTBearerTokenValidator, self).__init__(public_key)
        self.claims_options = {
            "exp": {"essential": True},
            "aud": {"essential": True, "value": audience},
            "iss": {"essential": True, "value": issuer},
        }


class Auth0Wrapper:
    def __init__(self):
        # Auth0 JWT validation
        self.require_auth = ResourceProtector()
        validator = Auth0JWTBearerTokenValidator(
            "dev-w5wu3a3y.us.auth0.com", "GroupFinderAPI"
        )
        self.require_auth.register_token_validator(validator)
