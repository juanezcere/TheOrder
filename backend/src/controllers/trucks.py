from flask import Blueprint, request, g, jsonify
import logging
import json
from src import database
from datetime import datetime
from src.helpers.generate_id import generate_id
from src.helpers.detect_changes import detect_changes

trucks = Blueprint('trucks', __name__)

@trucks.route('/', methods=['GET'])
def get_trucks_route():
    try:
        data = database.read(sql='SELECT * FROM trucks;')
        return jsonify({'code': '000', 'message': 'Get trucks successfully executed', 'data': data})
    except Exception as err:
        print(err)
        logging.warning('Error in get trucks. ' + str(err))
        return jsonify({'code': '001', 'message': 'Get trucks error. ' + str(err)})


@trucks.route('/', methods=['POST'])
def create_trucks_route():
    def validation(data):
        if not 'truck_name' in data:
            raise Exception('error', '002', 'No truck name specified')
        return True
    try:
        data = json.loads(request.data)
        validation(data)
        register = database.read(sql='SELECT truck_id FROM trucks WHERE truck_name=%s;', registers=[data['truck_name']])
        if len(register):
            raise Exception('error', '003', 'Truck already exists')
        data['truck_id'] = generate_id()
        sql = 'INSERT INTO trucks (truck_id, truck_name) VALUES (%s, %s);'
        register = (data['truck_id'], data['truck_name'])
        database.write(sql=sql, registers=[register])
        return jsonify({'code': '000', 'message': 'Create trucks successfully executed', 'data': data})
    except Exception as err:
        if len(err.args) == 3 and err.args[0] == 'error':
            return jsonify({'code': err.args[1], 'message': err.args[2]})
        print(err)
        logging.warning('Error in create trucks. ' + str(err))
        return jsonify({'code': '004', 'message': 'Create trucks error. ' + str(err)})


@trucks.route('/<register_id>', methods=['PUT'])
def update_trucks_route(register_id):
    def validation(data):
        if not 'truck_name' in data:
            raise Exception('error', '002', 'No truck name specified')
        return True
    try:
        data = json.loads(request.data)
        validation(data)
        register = database.read(sql='SELECT * FROM trucks WHERE truck_id=%s;', registers=[register_id])[0]
        if not len(register):
            raise Exception('error', '005', 'Truck not exists')
        changes = detect_changes(old_data=register, new_data=data)
        if not len(changes):
            raise Exception('error', '006', 'Register with same information')
        sql = 'UPDATE trucks SET truck_name=%s WHERE truck_id=%s;'
        register = (data['truck_name'], register_id)
        database.write(sql=sql, registers=[register])
        return jsonify({'code': '000', 'message': 'Update trucks successfully executed', 'data': data})
    except Exception as err:
        if len(err.args) == 3 and err.args[0] == 'error':
            return jsonify({'code': err.args[1], 'message': err.args[2]})
        print(err)
        logging.warning('Error in update clusters. ' + str(err))
        return jsonify({'code': '007', 'message': 'Update trucks error. ' + str(err)})


@trucks.route('/<register_id>', methods=['DELETE'])
def delete_trucks_route(register_id):
    try:
        data = json.loads(request.data)
        register = database.read(sql='SELECT * FROM trucks WHERE truck_id=%s;', registers=[register_id])
        if not len(register):
            raise Exception('error', '005', 'Truck not exists')
        sql = 'DELETE FROM trucks WHERE truck_id=%s;'
        register = (register_id)
        database.write(sql=sql, registers=[register])
        return jsonify({'code': '000', 'message': 'Delete trucks successfully executed', 'data': data})
    except Exception as err:
        print(err)
        logging.warning('Error in delete trucks. ' + str(err))
        return jsonify({'code': '008', 'message': 'Delete trucks error. ' + str(err)})
