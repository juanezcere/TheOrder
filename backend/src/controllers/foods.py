from flask import Blueprint, request, g, jsonify
import logging
import json
from src import database
from datetime import datetime
from src.helpers.generate_id import generate_id
from src.helpers.detect_changes import detect_changes

foods = Blueprint('foods', __name__)

@foods.route('/', methods=['GET'])
def get_foods_route():
    try:
        data = database.read(sql='SELECT * FROM foods;')
        return jsonify({'code': '000', 'message': 'Get foods successfully executed', 'data': data})
    except Exception as err:
        print(err)
        logging.warning('Error in get foods. ' + str(err))
        return jsonify({'code': '009', 'message': 'Get foods error. ' + str(err)})


@foods.route('/<register_id>', methods=['GET'])
def get_foods_by_truck_route(register_id):
    try:
        data = database.read(sql='SELECT * FROM foods WHERE truck_id=%s;', registers=[register_id])
        return jsonify({'code': '000', 'message': 'Get foods successfully executed', 'data': data})
    except Exception as err:
        print(err)
        logging.warning('Error in get foods. ' + str(err))
        return jsonify({'code': '010', 'message': 'Get foods error. ' + str(err)})


@foods.route('/', methods=['POST'])
def create_foods_route():
    def validation(data):
        if not 'food_name' in data:
            raise Exception('error', '011', 'No food name specified')
        if not 'truck_id' in data:
            raise Exception('error', '027', 'No truck specified')
        return True
    try:
        data = json.loads(request.data)
        validation(data)
        register = database.read(sql='SELECT food_id FROM foods WHERE food_name=%s;', registers=[data['food_name']])
        if len(register):
            raise Exception('error', '012', 'Food already exists')
        data['food_id'] = generate_id()
        data['food_value'] = data['food_value'] if 'food_value' in data else 0.0
        sql = 'INSERT INTO foods (food_id, food_name, food_value, truck_id) VALUES (%s, %s, %s, %s);'
        register = (data['food_id'], data['food_name'], data['food_value'], data['truck_id'])
        database.write(sql=sql, registers=[register])
        return jsonify({'code': '000', 'message': 'Create foods successfully executed', 'data': data})
    except Exception as err:
        if len(err.args) == 3 and err.args[0] == 'error':
            return jsonify({'code': err.args[1], 'message': err.args[2]})
        print(err)
        logging.warning('Error in create foods. ' + str(err))
        return jsonify({'code': '013', 'message': 'Create foods error. ' + str(err)})


@foods.route('/<register_id>', methods=['PUT'])
def update_foods_route(register_id):
    def validation(data):
        if not 'food_name' in data:
            raise Exception('error', '011', 'No food name specified')
        return True
    try:
        data = json.loads(request.data)
        validation(data)
        register = database.read(sql='SELECT * FROM foods WHERE food_id=%s;', registers=[register_id])[0]
        if not len(register):
            raise Exception('error', '014', 'Food not exists')
        changes = detect_changes(old_data=register, new_data=data)
        if not len(changes):
            raise Exception('error', '015', 'Register with same information')
        sql = 'UPDATE foods SET food_name=%s, food_value=%s WHERE food_id=%s;'
        register = (data['food_name'], data['food_value'], register_id)
        database.write(sql=sql, registers=[register])
        return jsonify({'code': '000', 'message': 'Update foods successfully executed', 'data': data})
    except Exception as err:
        if len(err.args) == 3 and err.args[0] == 'error':
            return jsonify({'code': err.args[1], 'message': err.args[2]})
        print(err)
        logging.warning('Error in update clusters. ' + str(err))
        return jsonify({'code': '016', 'message': 'Update foods error. ' + str(err)})


@foods.route('/<register_id>', methods=['DELETE'])
def delete_foods_route(register_id):
    try:
        data = json.loads(request.data)
        register = database.read(sql='SELECT * FROM foods WHERE food_id=%s;', registers=[register_id])
        if not len(register):
            raise Exception('error', '014', 'food not exists')
        sql = 'DELETE FROM foods WHERE food_id=%s;'
        register = (register_id)
        database.write(sql=sql, registers=[register])
        return jsonify({'code': '000', 'message': 'Delete foods successfully executed', 'data': data})
    except Exception as err:
        print(err)
        logging.warning('Error in delete foods. ' + str(err))
        return jsonify({'code': '017', 'message': 'Delete foods error. ' + str(err)})
