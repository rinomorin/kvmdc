import jwt
from flask import request, g, jsonify, session
from datetime import datetime, timedelta
from flask import current_app as app
from functools import wraps
from models.I_LoadConfig import revoked_tokens


def Get_Header_Item(item, default=None):
    all_headers = dict(g.flask_request.headers)
    if item in all_headers:
        return all_headers[item]
    else:
        return None


def Logout():
    # Access the request object directly
    all_headers = dict(request.headers)
    if 'Authorization' in all_headers:
        # Get the token from the request headers
        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header.split("Bearer ")[1]
            # Invalidate or remove the token
            revoked_tokens.add(token)
            # Optionally, remove the token from the g object
            # if it was set there during login
            g.pop('token', None)
            new_headers = dict(request.headers)
            if 'Authorization' in new_headers:
                del new_headers['Authorization']
            # Update the request headers with the new dictionary
            request.headers = new_headers
            # del request.headers['Authorization']
            print(revoked_tokens)
            return "{You've been successfully logout. }"
        else:
            return all_headers
    else:
        return "Logout Fails or You where not logged in"


def GetAuthorize(item, thisHeader):
    if thisHeader:
        try:
            token = thisHeader.split(' ')[1]
            decoded_token = jwt.decode(
                token, app.config['SECRET_KEY'], algorithms=['HS256']
            )
            rc_item = decoded_token.get(item)
            if item == "token":
                return token
            else:
                return rc_item
        except jwt.ExpiredSignatureError:
            session.pop('user_id', None)
            return "Expired Token. Please log in again."
        except jwt.InvalidTokenError:
            return "Invalid Token. Please log in again."
    else:
        return None


def Login(users_collection):
    # global users_collection
    # Get username and password from request data
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    print(username, password)
    print(users_collection)

    user = users_collection.find_one(
        {'username': username, 'password': password}
        )

    if user:
        # Generate JWT token
        token_payload = {
            'username': username,
            'exp': datetime.utcnow() + timedelta(days=1)
        }
        token = jwt.encode(
            token_payload, app.config['SECRET_KEY'], algorithm='HS256'
            )

        # Create response headers with bearer token
        headers = {'Authorization': f'Bearer {token}'}
        session['user_id'] = username
        # Return token and headers as part of the GraphQL response
        return token, headers
    else:
        return 'Invalid username or password', {}


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return jsonify({'error': 'Unauthorized'}), 401
        return f(*args, **kwargs)
    return decorated_function
