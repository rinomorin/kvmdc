import jwt
from datetime import datetime, timedelta
from models.I_LoadConfig import SECRET_KEY

token_vars = set
# app = LoadConfig(current_app)
# THIS_SECRET_KEY = current_app.config.get['SECRET_KEY']
# global MySecret
# print(__it_a_secret__)

# def __setitem__(key, value):
#     token_vars[key] = value


# def __getitem__(key):
#     return token_vars[key]

THIS_SECRET_KEY = SECRET_KEY
ALGORITHM = 'HS256'
EXPIRATION_TIME_MINUTES = 30


def generate_token(user_id: int) -> str:
    payload = {
        'user_id': user_id,
        'exp': datetime.utcnow() + timedelta(minutes=EXPIRATION_TIME_MINUTES)
    }
    return jwt.encode(payload, THIS_SECRET_KEY, algorithm=ALGORITHM)


def verify_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        return {'error': 'Token has expired'}
    except jwt.InvalidTokenError:
        return {'error': 'Invalid token'}


def revoke_token(token: str):
    # Add logic to revoke token (e.g., add to blacklist,
    # remove from active tokens, etc.)
    pass
