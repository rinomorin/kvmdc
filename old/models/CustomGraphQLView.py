from flask import request, g, jsonify
from flask_graphql import GraphQLView


class CustomGraphQLView(GraphQLView):
    def get_context(self):
        try:
            context = super().get_context()
            g.flask_request = request
            return context
        except Exception as e:
            # Handle the exception here
            return jsonify({'error': str(e)}), 500
