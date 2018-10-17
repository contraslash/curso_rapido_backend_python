import jwt
from jwt.exceptions import PyJWTError
import datetime
from django.conf import LazySettings

settings = LazySettings()


def create_jwt_token_for_user(user):
    payload = dict()
    now = datetime.datetime.utcnow()
    payload.update(
        {
            "exp": now + datetime.timedelta(hours=settings.JWT_VALIDITY_TIME),
            "nbf": now,
            "iss": "auth.devhack-python-2018-i",
            "aud": "*.devhack-python-2018-i",
            "iat": now,
            "name": "{} {}".format(user.first_name, user.last_name),
            "given_name": user.first_name,
            "family_name": user.last_name,
            "email": user.email,
            "preferred_username": user.username
        }
    )

    return jwt.encode(payload, settings.JWT_HS256_KEY)

def token_is_valid(token):
    try:

        jwt.decode(token, settings.JWT_HS256_KEY, audience=["*.devhack-python-2018-i"])
        return True
    except PyJWTError:
        return False