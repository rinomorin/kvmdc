from models.routes import app

if __name__ == '__main__':
    app.run(
        debug=True, port=4000, ssl_context=(
            'ssl/GraphQL.pem', 'ssl/GraphQL.pem'
            )
    )
