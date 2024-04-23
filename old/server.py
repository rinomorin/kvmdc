from flask import Flask, request, jsonify
import graphene
from graphene import String
from models.I_LoadConfig import LoadConfig, Loggit
from models.CustomGraphQLView import CustomGraphQLView
from models.I_Mongo import MongoDB
from models import query, mutation
from resolvers import query_resolver
from models.I_Auth import Login, login_required, Logout
from resolvers.mutation_resolver import resolve_add_user


app = Flask(__name__)
app = LoadConfig(app)
mongo = MongoDB()
mongo.__setitem__('mongo_url', app.config['mongo_url'])
mongo.__setitem__('mongo_client', app.config['mongo_client'])
db = mongo.MongoConnect()
loggit = Loggit(app)
loggit.Set_DB(db)
users_collection = db['users']


@app.route('/home')
@app.route('/', methods=['GET'])
def home():
    # Get all headers from the request
    headers = dict(request.headers)
    return jsonify(headers)


@app.route('/login', methods=['POST'])
def login_route():
    return Login(users_collection)


# SECURED SECTION
# Logout route
@app.route('/logout', methods=['POST'])
@login_required
def logout():
    success = String()
    del success
    return Logout()


schema = graphene.Schema(query=query.Query, mutation=mutation.Mutation)
query.Query._meta.fields['hello'].resolver = query_resolver.resolve_hello
mutation.Mutation._meta.fields['add_user'].resolver = resolve_add_user

app.add_url_rule(
    '/graphql', view_func=CustomGraphQLView.as_view(
        'graphql', schema=schema, graphiql=True
        )
    )

if __name__ == '__main__':
    app.run(
        debug=True, port=4000, ssl_context=(
            'ssl/GraphQL.pem', 'ssl/GraphQL.pem'
            )
        )
