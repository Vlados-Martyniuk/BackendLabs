from flask import Flask
from flask import jsonify
from flask import request
from datetime import datetime

app = Flask(__name__)

# Дані в пам'яті
users = {}
categories = {}
records = {}

# Counter для ідентифікаторів
user_id_counter = 1
category_id_counter = 1
record_id_counter = 1

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    response = {
        "status": "OK",
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return jsonify(response), 200

# 1. Ендпоінти для користувачів
@app.route('/user', methods=['POST'])
def create_user():
    global user_id_counter
    data = request.json
    user = {
        'id': user_id_counter,
        'name': data.get('name')
    }
    users[user_id_counter] = user
    user_id_counter += 1
    return jsonify(user), 201

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user)

@app.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({'error': 'User not found'}), 404
    del users[user_id]
    return '', 204

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(list(users.values()))

# 2. Ендпоінти для категорій
@app.route('/category', methods=['POST'])
def create_category():
    global category_id_counter
    data = request.json
    category = {
        'id': category_id_counter,
        'name': data.get('name')
    }
    categories[category_id_counter] = category
    category_id_counter += 1
    return jsonify(category), 201

@app.route('/category', methods=['GET'])
def get_categories():
    return jsonify(list(categories.values()))

@app.route('/category/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    if category_id not in categories:
        return jsonify({'error': 'Category not found'}), 404
    del categories[category_id]
    return '', 204

# 3. Ендпоінти для записів
@app.route('/record', methods=['POST'])
def create_record():
    global record_id_counter
    data = request.json
    if data.get('user_id') not in users:
        return jsonify({'error': 'User not found'}), 404
    if data.get('category_id') not in categories:
        return jsonify({'error': 'Category not found'}), 404
    record = {
        'id': record_id_counter,
        'user_id': data.get('user_id'),
        'category_id': data.get('category_id'),
        'timestamp': datetime.now().isoformat(),
        'amount': data.get('amount')
    }
    records[record_id_counter] = record
    record_id_counter += 1
    return jsonify(record), 201

@app.route('/record/<int:record_id>', methods=['GET'])
def get_record(record_id):
    record = records.get(record_id)
    if not record:
        return jsonify({'error': 'Record not found'}), 404
    return jsonify(record)

@app.route('/record/<int:record_id>', methods=['DELETE'])
def delete_record(record_id):
    if record_id not in records:
        return jsonify({'error': 'Record not found'}), 404
    del records[record_id]
    return '', 204

@app.route('/record', methods=['GET'])
def get_records():
    user_id = request.args.get('user_id', type=int)
    category_id = request.args.get('category_id', type=int)

    if not user_id and not category_id:
        return jsonify({'error': 'User ID or Category ID is required'}), 400

    filtered_records = [
        record for record in records.values()
        if (not user_id or record['user_id'] == user_id) and
           (not category_id or record['category_id'] == category_id)
    ]

    return jsonify(filtered_records)

