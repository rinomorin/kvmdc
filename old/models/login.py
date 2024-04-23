from graphene import ObjectType
from flask import request
from models.I_Auth import Login


class login(ObjectType):
    def __init__(self):
        return Login(request)
