# server.py
from flask import Flask, request
from rdpy.protocol.rdp import RDPClient
import paramiko

app = Flask(__name__)

@app.route('/connect', methods=['POST'])
def connect_to_host():
    data = request.json
    hostname = data['hostname']
    host_type = data['host_type']

    if host_type == 'windows':
        # Establish RDP connection with virtual keyboard options
        rdp = RDPClient(hostname, 3389)  # 3389 is the default RDP port
        rdp.connect()
        rdp.login(username, password)

        # Example: Send Ctrl+Alt+Del keyboard combination
        rdp.send_keyboard_event('ctrl', True)
        rdp.send_keyboard_event('alt', True)
        rdp.send_keyboard_event('delete', True)
        rdp.send_keyboard_event('delete', False)
        rdp.send_keyboard_event('alt', False)
        rdp.send_keyboard_event('ctrl', False)

        rdp.disconnect()

        return 'RDP connection established with virtual keyboard options'
    elif host_type == 'linux':
        # Establish SSH connection to Linux host
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname, username='your_username', password='your_password')

        # Example: Run a command on the Linux host
        stdin, stdout, stderr = ssh.exec_command('ls -l')

        # Read the command output
        output = stdout.read().decode('utf-8')

        # Close the SSH connection
        ssh.close()

        return output
    else:
        return 'Invalid host type'

if __name__ == "__main__":
    app.run(debug=True)
