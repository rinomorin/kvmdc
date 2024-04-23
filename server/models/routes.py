from flask import Flask, jsonify, request
import graphene
import subprocess
from graphene import String
from flask_graphql import GraphQLView
from models.mongodbApi import db
from models.auth import Login, login_required, Logout, VerifyMfa, Get_UserID
from models.kvmconfig import KVMDC_Config
from models.Query import Query
from models.mutation import Mutation
import pyotp
import qrcode
from io import BytesIO
import base64


# from models.mutation_resolver import ResolvRegistration,  schema
app = Flask(__name__)
app.secret_key = KVMDC_Config['ssl']['secret']
# Check if already connected
if not db.client:
    db.connect()
    db_logging_api = "models/mongo_logging.py"
    if not db.is_process_running(db_logging_api):
        db.start_external_script(db_logging_api)

    if db.count_collections() ==  0:
        try:
            # Execute the external script
            subprocess.run(["python", "models/init_db_users.py"], check=True)
            print("External script executed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error executing external script: {e}")
    # print("db counr",count)
else:
    print("Already connected to MongoDB")


@app.route('/home')
@app.route('/', methods=['GET'])
def home():
    # Get all headers from the request
    headers = dict(request.headers)
    return jsonify(headers)


@app.route('/login', methods=['POST'])
def login_route():
    return Login()


@app.route('/verify-mfa', methods=['POST'])
def verify_route():
    return VerifyMfa()


schema = graphene.Schema(query=Query, mutation=Mutation)


@app.route('/registration', methods=['POST'])
# def registration():
def register_user():
    # Generate a secret key for the user
    secret_key = KVMDC_Config["OTP_SECRET"]
    # secret_key = pyotp.random_base32()
    # store key in user db
    username = Get_UserID()
    print(username)
    username = "test_user"
    # Generate the OTP URL for Google Authenticator
    otp_url = pyotp.totp.TOTP(secret_key).provisioning_uri( 
        username
        , issuer_name='KVMDC'
        )
 
    # Generate the QR code
    qr = qrcode.make(otp_url)

    # Convert the QR code image to bytes
    qr_byte_stream = BytesIO()
    qr.save(qr_byte_stream, format='PNG')
    qr_byte_stream.seek(0)
    qr_base64 = base64.b64encode(qr_byte_stream.read()).decode('utf-8')
    return jsonify(
        {'secret_key': secret_key, 'otp_url': otp_url, 'qr_code': qr_base64}
        )


@app.route('/logout', methods=['POST'])
@login_required
def logout():
    success = String()
    del success
    return Logout()


# Define GraphQL view
app.add_url_rule('/graphql',
                 view_func=GraphQLView.as_view('graphql',
                                               schema=schema,
                                               graphiql=True
                                               ))
