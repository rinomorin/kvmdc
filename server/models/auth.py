import jwt
from flask import request, jsonify, session, g
from datetime import datetime, timedelta
from functools import wraps
from models.kvmconfig import KVMDC_Config, revoked_tokens
from models.mongodbApi import db
import pyotp


def Login():
    return DCAuthenticate.Login(db)


def VerifyMfa():
    return DCAuthenticate.VerifyMfa(db)


def login_required(f):
    return DCAuthenticate.login_required(f)


def Logout():
    return DCAuthenticate.Logout()

def Get_UserID():
    return DCAuthenticate.get_userid(db)

class DCAuthenticate:
    def __init__(self):
        pass

    def get_userid(db):
        # Get username and password from request data
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        user = db.find_one('users',
                           {'username': username, 'password': password}
                           )
        print("get_userid", username, user)
        if user:
            return user['username']
        else:
            return "invalide userid"

    def Login(db):
        # global users_collection
        # Get username and password from request data
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        print("user", username, password)
        user = db.find_one('users',
                           {'username': username, 'password': password}
                           )
        if user:
            kvm_secret = KVMDC_Config['ssl']['secret']
            # Generate JWT token
            token_payload = {
                'username': username,
                'exp': datetime.utcnow() + timedelta(days=1)
            }
            token = jwt.encode(
                token_payload, kvm_secret, algorithm='HS256'
                )

            # Create response headers with bearer token
            headers = {'Authorization': f'Bearer {token}'}
            session['user_id'] = username
            # Return token and headers as part of the GraphQL response
            return token, headers
        else:
            return 'Invalid username or password', {}

    def VerifyMfa(db):
        data = request.json
        username = data.get('username')
        password = data.get('password')
        code = data.get('code')
        if not (username and code):
            return jsonify({'error': 'Username and code are required'}), 400

        user = db.find_one('users',
                           {'username': username, 'password': password}
                           )
        print(user)
        if user is None:
            return jsonify({'error': 'User not found'}), 404
        print("login", user)

        user_secret_key = KVMDC_Config["OTP_SECRET"]
        totp = pyotp.TOTP(user_secret_key)
        print("codes", code, user_secret_key)
        if totp.verify(int(code)):
            return jsonify({'message': '2FA code verified. Login successful!'})
        else:
            print("fail", code, user_secret_key)
            return jsonify({'error': 'Invalid 2FA code'}), 401

    def login_required(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'user_id' not in session:
                return jsonify({'error': 'Unauthorized'}), 401
            return f(*args, **kwargs)
        return decorated_function

    def is_logged_in():
        all_headers = dict(request.headers)
        if 'Authorization' in all_headers:
            # Get the token from the request headers
            auth_header = request.headers.get('Authorization')
            if auth_header and auth_header.startswith("Bearer "):
                token = auth_header.split("Bearer ")[1]
                return token
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
                print("rev", revoked_tokens)
                # Optionally, remove the token from the g object
                # if it was set there during login
                g.pop('token', None)
                new_headers = dict(request.headers)
                if 'Authorization' in new_headers:
                    del new_headers['Authorization']
                # Update the request headers with the new dictionary
                request.headers = new_headers
                # del request.headers['Authorization']
                return "{You've been successfully logout. }"
            else:
                return all_headers
        else:
            return "Logout Fails or You where not logged in"

    def GetAuthorize(item, thisHeader):
        kvm_secret = KVMDC_Config['ssl']['secret']
        if thisHeader:
            try:
                token = thisHeader.split(' ')[1]
                decoded_token = jwt.decode(
                    token, kvm_secret, algorithms=['HS256']
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

    def Get_Header_Item(item, default=None):
        all_headers = dict(g.flask_request.headers)
        if item in all_headers:
            return all_headers[item]
        else:
            return None
