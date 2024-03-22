# server.py (Flask backend)

from flask import Flask, jsonify
import libvirt


app = Flask(__name__)

def connect_to_hypervisor():
    # Connect to the KVM hypervisor
    conn = libvirt.open("qemu+ssh://lv-user@192.168.100.3/system")
    if conn is None:
        raise Exception("Failed to connect to the KVM hypervisor")
    return conn

@app.route('/vms')
def list_vms():
    try:
        # Connect to the hypervisor
        conn = connect_to_hypervisor()
        # Get list of all running VMs
        vms = conn.listDomainsID()
        return jsonify({'vms': vms})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/pools')
def list_pools():
    try:
        # Connect to the hypervisor
        conn = connect_to_hypervisor()
        # Get list of all running VMs
        pools = conn.listNetworks()
        return jsonify({'pools': pools})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/console/<int:vm_id>')
def console_connection(vm_id):
    try:
        # Connect to the hypervisor
        conn = connect_to_hypervisor()
        # Lookup the VM by ID
        vm = conn.lookupByID(vm_id)
        # Open a console connection to the VM
        console = vm.console()
        # Perform any additional operations with the console
        # For example, you might want to read from or write to the console here
        return jsonify({'message': 'Console connection established'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True,port=5001,host="192.168.100.3")
