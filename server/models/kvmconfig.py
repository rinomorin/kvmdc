import os
import sys
import jwt
import base64
from datetime import datetime, timedelta
import subprocess
import json
import getpass
import threading
import time
# import signal


# from cryptography.fernet import Fernet
config_path = None
registration_database = {}
revoked_tokens = set()
KVMDC_Config = {}


class KVMdcConfig:

    def __init__(self):
        if len(sys.argv) > 1:
            conf_file = sys.argv[1]
        else:
            ThisFile = os.path.dirname(os.path.abspath(__file__))
            conf_file = str(os.path.dirname(ThisFile))
            conf_file = conf_file + "/config/kvmdc.json"
        KVMDC_Config['config'] = {}
        KVMDC_Config['ssl'] = {}
        KVMDC_Config['dbm'] = {}
        KVMDC_Config['config']['Config_File'] = conf_file
        config_folder = os.path.dirname(conf_file)
        self.config_file = os.path.basename(conf_file)
        self.base_name, _ = os.path.splitext(self.config_file)
        json_file = str(self.base_name+".json")
        self.json_file = os.path.join(config_folder, json_file)

    def ConfigExists(self):
        confile = KVMDC_Config["config"]["Config_File"]
        if not os.path.exists(confile):
            self.create_config_file()
        else:
            self.read_config_file()

    def get_dbm_id_token(self):
        # Prompt user for parameters
        username = input("Enter db username: ")
        password = getpass.getpass("Enter password: ")
        dbcon = input("mongo connection: ")
        dbname = input("mongo default database: ")
        return self.generate_token(username, password, dbcon, dbname)
        # You can add more parameters as needed

    def create_config_file(self):
        confile = KVMDC_Config['config']['Config_File']
        config_folder = os.path.dirname(confile)
        # Prompt user for encryption password
        print("IMPORTANT: Remember to store your password in save"
              + " location. it cannot be recovered!")
        encryption_password = input("Enter encryption password: ")
        oc = openssl_crypting()
        oc.encrypt_string(encryption_password)
        # Encrypt the string
        KVMDC_Config["dbm"]["Authorization"] = str(self.get_dbm_id_token())
        KVMDC_Config["OTP_SECRET"] = pyotp.random_base32()
        # Save dictionary as JSON file
        if not os.path.exists(config_folder):
            os.makedirs(config_folder)
        with open(self.json_file, 'w') as json_file:
            json.dump(KVMDC_Config, json_file)
        print("JSON file saved successfully.")

    def get_item_from_token(self, token, item):
        secret_key = KVMDC_Config['ssl']['secret']
        try:
            decoded_token = jwt.decode(token, secret_key, algorithms=['HS256'])
            return decoded_token.get(item)
        except jwt.ExpiredSignatureError:
            return "Token expired"
        except jwt.InvalidTokenError:
            return "Invalid token"

    def generate_token(self, username, password, dbcon, dbname):
        # Define payload (data to be included in the token)
        payload = {
            'username': username,
            'password': password,
            'dbcon': dbcon,
            'dbname': dbname,
            'exp': datetime.utcnow() + timedelta(days=365)
        }

        # Define secret key (change this to a secure random key in production)
        secret_key = KVMDC_Config['ssl']['secret']
        # Generate the token
        token = jwt.encode(payload, secret_key, algorithm='HS256')

        return token

    def read_config_file(self):
        config_file = KVMDC_Config['config']['Config_File']
        print("Loading config " + self.base_name + " file parameters...")

        # Read parameters from the config file
        with open(config_file, "r") as f:
            config_data = json.load(f)
            this_secret = config_data['ssl']['secret']
            this_key_file = config_data['ssl']['key_file']
            this_Authorization = config_data['dbm']['Authorization']
            this_company = config_data['Company']
            otp_secret = config_data['OTP_SECRET']
        KVMDC_Config["Company"] = this_company
        KVMDC_Config['ssl']['secret'] = this_secret
        KVMDC_Config['ssl']['key_file'] = this_key_file
        KVMDC_Config['dbm']['Authorization'] = this_Authorization
        KVMDC_Config["OTP_SECRET"] = otp_secret


class openssl_crypting:

    def __init__(self):
        KVMDC_Config['ssl'] = {}
        confile = KVMDC_Config["config"]["Config_File"]
        config_folder = os.path.dirname(confile)
        self.config_file = os.path.basename(confile)
        self.base_name, _ = os.path.splitext(self.config_file)
        self.key_file = os.path.join(config_folder, str(self.base_name+".key"))
        self.generate_key(self.key_file)

    def generate_key(self, key_file):
        # Generate a random key using OpenSSL
        openssl_process = subprocess.Popen(
            ["openssl", "rand", "-out", self.key_file, "32"],
            # Generate a 256-bit (32-byte) key
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        openssl_process.communicate()
        KVMDC_Config['ssl']['key_file'] = key_file

    def encrypt_string(self, myString):
        # Generate a random string
        data = os.urandom(4096)
        # Encrypt the string
        encrypted_data = self.encryption_string(data, self.key_file, myString)
        return encrypted_data

    def encryption_string(self, data, key_file, password):
        # Create a subprocess to run openssl command
        openssl_process = subprocess.Popen(
            ["openssl", "enc", "-aes-256-cbc", "-pbkdf2", "-pass",
             f"pass:{password}", "-kfile", key_file, "-e"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        # Communicate with the subprocess: pass data and retrieve
        # the encrypted output
        encrypted_data, _ = openssl_process.communicate(input=data)
        # Convert encrypted and decrypted data to Base64
        base64_encrypted_data = base64.b64encode(encrypted_data)
        KVMDC_Config['ssl']['secret'] = base64_encrypted_data.decode('ascii')
        return

    def decrypt_string(self, myString, password):
        # Decode Base64-encoded encrypted data
        encrypted_data = base64.b64decode(myString)
        # print("encrypt: " + str(encrypted_data))
        key_file = KVMDC_Config['ssl']['key_file']
        data = self.decrypt_datastring(encrypted_data, key_file, password)
        return data

    def decrypt_datastring(self, encrypted_data, key_file, password):
        # Create a subprocess to run openssl command
        openssl_process = subprocess.Popen(
            ["openssl", "enc", "-aes-256-cbc", "-pbkdf2", "-pass",
             f"pass:{password}", "-kfile", key_file, "-d"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        # Communicate with the subprocess: pass encrypted data and retrieve
        # the decrypted output
        decrypted_data, _ = openssl_process.communicate(input=encrypted_data)
        return decrypted_data


class ExternalScriptRunner:
    def __init__(self):
        self.process = None
        self.thread = None
        self.stop_event = threading.Event()
        self.restart_event = threading.Event()

    def run_external_script(self):
        # Command to run the external script
        command = ['python', 'mongo_logging.py']

        while not self.stop_event.is_set():
            # Run the external script detached from the parent process
            self.process = subprocess.Popen(
                command, stdout=subprocess.PIPE,
                stderr=subprocess.PIPE, stdin=subprocess.PIPE,
                start_new_session=True)

            # Wait for the process to finish or stop event to be set
            while self.process.poll() is None and not self.stop_event.is_set():
                time.sleep(1)

            # Clean up the process
            if self.process.poll() is None:
                self.process.terminate()
                self.process.wait()

            # Restart the thread if requested
            if self.restart_event.is_set():
                self.restart_event.clear()
            else:
                break

    def start(self):
        # Create a thread to run the external script
        self.thread = threading.Thread(target=self.run_external_script)

        # Start the thread
        self.thread.start()

    def stop(self):
        # Set stop event to terminate the external script
        self.stop_event.set()

    def restart(self):
        # Set restart event to restart the thread
        self.restart_event.set()
        self.stop()


KVMdcConfig().ConfigExists()
