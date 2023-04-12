from flask import Blueprint, request, g, jsonify
import logging
import json
from src import database
from datetime import datetime
from src.helpers.generate_id import generate_id
from src.helpers.detect_changes import detect_changes

orders = Blueprint('orders', __name__)

@orders.route('/', methods=['GET'])
def get_orders_route():
    try:
        data = database.read(sql='SELECT * FROM orders INNER JOIN foods ON orders.food_id = foods.food_id ORDER BY order_date ASC;')
        return jsonify({'code': '000', 'message': 'Get orders successfully executed', 'data': data})
    except Exception as err:
        print(err)
        logging.warning('Error in get orders. ' + str(err))
        return jsonify({'code': '018', 'message': 'Get orders error. ' + str(err)})


@orders.route('/<register_id>', methods=['GET'])
def get_orders_by_truck_route(register_id):
    try:
        data = database.read(sql='SELECT * FROM orders INNER JOIN foods ON orders.food_id = foods.food_id WHERE foods.truck_id=%s ORDER BY order_date ASC;', registers=[register_id])
        return jsonify({'code': '000', 'message': 'Get orders successfully executed', 'data': data})
    except Exception as err:
        print(err)
        logging.warning('Error in get orders. ' + str(err))
        return jsonify({'code': '019', 'message': 'Get orders error. ' + str(err)})


@orders.route('/', methods=['POST'])
def create_orders_route():
    def validation(data):
        if not 'food_id' in data:
            raise Exception('error', '020', 'No food specified')
        if not 'customer' in data:
            raise Exception('error', '021', 'No customer specified')
        return True
    try:
        data = json.loads(request.data)
        validation(data)
        data['order_id'] = generate_id()
        data['food_quantity'] = data['food_quantity'] if 'food_quantity' in data else 1
        data['observations'] = data['observations'] if 'observations' in data else ''
        data['where_eat'] = data['where_eat'] if 'where_eat' in data else False
        sql = 'INSERT INTO orders (order_id, food_id, customer, food_quantity, observations, where_eat) VALUES (%s, %s, %s, %s, %s, %s);'
        register = (data['order_id'], data['food_id'], data['customer'], data['food_quantity'], data['observations'], data['where_eat'])
        database.write(sql=sql, registers=[register])
        return jsonify({'code': '000', 'message': 'Create orders successfully executed', 'data': data})
    except Exception as err:
        if len(err.args) == 3 and err.args[0] == 'error':
            return jsonify({'code': err.args[1], 'message': err.args[2]})
        print(err)
        logging.warning('Error in create orders. ' + str(err))
        return jsonify({'code': '022', 'message': 'Create orders error. ' + str(err)})


@orders.route('/<register_id>', methods=['PUT'])
def update_orders_route(register_id):
    try:
        data = json.loads(request.data)
        register = database.read(sql='SELECT * FROM orders WHERE order_id=%s;', registers=[register_id])[0]
        if not len(register):
            raise Exception('error', '023', 'Order not exists')
        data['food_quantity'] = data['food_quantity'] if 'food_quantity' in data else 1
        data['observations'] = data['observations'] if 'observations' in data else ''
        data['status'] = data['status'] if 'status' in data else 0
        data['where_eat'] = data['where_eat'] if 'where_eat' in data else False
        changes = detect_changes(old_data=register, new_data=data)
        if not len(changes):
            raise Exception('error', '024', 'Register with same information')
        sql = 'UPDATE orders SET food_id=%s, customer=%s, food_quantity=%s, observations=%s, status=%s, where_eat=%s WHERE order_id=%s;'
        register = (data['food_id'], data['customer'], data['food_quantity'], data['observations'], data['status'], data['where_eat'], register_id)
        database.write(sql=sql, registers=[register])
        return jsonify({'code': '000', 'message': 'Update orders successfully executed', 'data': data})
    except Exception as err:
        if len(err.args) == 3 and err.args[0] == 'error':
            return jsonify({'code': err.args[1], 'message': err.args[2]})
        print(err)
        logging.warning('Error in update clusters. ' + str(err))
        return jsonify({'code': '025', 'message': 'Update orders error. ' + str(err)})


@orders.route('/<register_id>', methods=['DELETE'])
def delete_orders_route(register_id):
    try:
        data = json.loads(request.data)
        register = database.read(sql='SELECT * FROM orders WHERE order_id=%s;', registers=[register_id])
        if not len(register):
            raise Exception('error', '023', 'Order not exists')
        sql = 'DELETE FROM orders WHERE order_id=%s;'
        register = (register_id)
        database.write(sql=sql, registers=[register])
        return jsonify({'code': '000', 'message': 'Delete orders successfully executed', 'data': data})
    except Exception as err:
        print(err)
        logging.warning('Error in delete orders. ' + str(err))
        return jsonify({'code': '026', 'message': 'Delete orders error. ' + str(err)})
