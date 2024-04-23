from models import token
from models.I_Auth import Login
from flask import request


def resolve_login(root, info, username, password):
    # Example authentication logic
    # (replace with your actual authentication logic)
    Login(request)
    if username == 'admin' and password == 'password':
        tok = token.generate_token(1)  # Generate token for user with user_id=1
        return {'token': tok}
    else:
        return {'token': None}

# def resolve_login(root, info, username, password):
#     # Example authentication logic
# (replace with your actual authentication logic)
#     if username == 'admin' and password == 'password':
#         token = generate_token(1)  # Generate token for user with user_id=1
#         return {'token': token}
#     else:
#         return {'token': None}
