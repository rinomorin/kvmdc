from graphene import ObjectType, String


class Query(ObjectType):
    hello = String(name=String(default_value="World"))

    def resolve_hello(root, info, name):
        return f'Hello {name}'
    
    def get_db_user(root,info,name):
        return f'username'
