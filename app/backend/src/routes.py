from flask import jsonify
from src import app
from .data import transport_data

# return all transports
@app.route('/transport', methods=['GET'])
def get_transport():
    return jsonify(transport_data)

# return transport with the specified id
@app.route('/transport/<int:transport_id>', methods=['GET'])
def get_transport_by_id(transport_id):
    transport = next((item for item in transport_data if item['id'] == transport_id), None)
    if transport:
        return jsonify(transport)
    else:
        return jsonify({'error': 'Transport not found'}), 404