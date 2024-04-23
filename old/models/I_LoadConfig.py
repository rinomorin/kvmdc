import logging
import datetime
# from datetime import timedelta
import pymongo
SECRET_KEY = 'your_secret_key'
revoked_tokens = set()
registration_database = {}


def LoadConfig(app):
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['mongo_url'] = 'mongodb://localhost:27017/'
    app.config['mongo_client'] = 'datacenter'
    app.config['logs_db'] = "logs"
    return app


class Loggit:
    def __init__(self, app):
        self.db = None
        self.logs_collection = app.config['logs_db']
        pass

    def Set_DB(self, db):
        self.db = db

    def ini_collector(self):
        self.logs_collection = self.db['logs_db']
        logs_collection = self.logs_collection
        # Create a logger
        logger = logging.getLogger(__name__)

        # Create the logs collection with the defined schema
        logs_collection.create_index([("_id", pymongo.ASCENDING)], unique=True)
        # Configure logging
        logging.basicConfig(level=logging.DEBUG)

        init_logs = {
            "error_date": datetime.datetime.now(),
            "error_code": "err_00000",
            "error_message": "initial setup",
            "error_caller": "loggit",
            "error_line": None,
            "error_user": "admin"
        }

        try:
            logs_collection.insert_one(init_logs)
            print("Initial setup successfully.")
        except pymongo.errors.DuplicateKeyError:
            print("Error: setup already exists.")
        except Exception as e:
            print("Error:", e)

        # Configure logging
        logging.basicConfig(level=logging.DEBUG)
        logger("err_00000", "initial setup", "loggit", None, "admin")

    def loggit(self, err_code=None, err_msg=None,
               err_callout=None, err_line=None):
        # Log a debug message
        log_stamp = datetime.datetime.now()
        self.logger.debug(
            "{log_stamp}::{err_code}::{err_callout}::{err_line}::{err_msg}"
            )
        self.loggit_to_db(log_stamp, err_code, err_msg, err_callout, err_line)
        # Your function logic here
        pass

    def loggit_to_db(
            self, err_code=None, err_msg=None, err_callout=None, err_line=None
            ):
        logs_collection = self.logs_collection
        msg_logs = {
            "error_date": datetime.now(),
            "error_code": "err_00000",
            "error_message": "initial setup",
            "error_caller": "loggit",
            "error_line": None,
            "error_user": "admin"
        }

        try:
            logs_collection.insert_one(msg_logs)
            print("Initial setup successfully.")
        except pymongo.errors.DuplicateKeyError:
            print("Error: setup already exists.")
        except Exception as e:
            print("Error:", e)
