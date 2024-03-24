import json

def load_data():
    data_path = '../data.json'
    with open(data_path, 'r') as file:
        data = json.load(file)
    return data.get('transport', [])

transport_data = load_data()