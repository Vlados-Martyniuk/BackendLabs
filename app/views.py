from flask import jsonify, request
from marshmallow import ValidationError
from app import db
from app.models import User, Category, Record, Currency
from app.schemas import UserSchema, CategorySchema, RecordSchema, CurrencySchema
from datetime import datetime
from flask_smorest import Blueprint


bp = Blueprint("api", __name__, url_prefix="/api")

# Ініціалізація схем
user_schema = UserSchema()
category_schema = CategorySchema()
record_schema = RecordSchema()
currency_schema = CurrencySchema()

# Обробка глобальних помилок
@bp.errorhandler(ValidationError)
def handle_validation_error(e):
    return jsonify({"error": "Validation Error", "messages": e.messages}), 400

@bp.errorhandler(Exception)
def handle_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "message": str(e),
    }), 500

@bp.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404

@bp.errorhandler(400)
def bad_request(e):
    return jsonify(error=str(e)), 400


@bp.route('/')
def hello_world():
    return 'Hello, World!'


@bp.route('/healthcheck', methods=['GET'])
def healthcheck():
    response = {
        "status": "OK",
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return jsonify(response), 200


# 1. Ендпоінти для користувачів
@bp.route('/user', methods=['POST'])
def create_user():
    data = request.json
    try:
        validated_data = user_schema.load(data)  # Валідація даних

        user = User(**validated_data)
        db.session.add(user)
        db.session.commit()

        return jsonify(user_schema.dump(user)), 201
    except ValidationError as e:
        return jsonify({"error": e.messages}), 400


@bp.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user_schema.dump(user))


@bp.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    db.session.delete(user)
    db.session.commit()
    return '', 204


@bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify(user_schema.dump(users, many=True))


# 2. Ендпоінти для категорій
@bp.route('/category', methods=['POST'])
def create_category():
    data = request.json
    try:
        validated_data = category_schema.load(data)

        category = Category(**validated_data)
        db.session.add(category)
        db.session.commit()

        return jsonify(category_schema.dump(category)), 201

    except ValidationError as e:
        return jsonify({"error": e.messages}), 400

@bp.route('/category', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    return jsonify(category_schema.dump(categories, many=True))


@bp.route('/category/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    category = Category.query.get(category_id)
    if not category:
        return jsonify({'error': 'Category not found'}), 404

    db.session.delete(category)
    db.session.commit()
    return '', 204


# 3. Ендпоінти для записів
@bp.route('/record', methods=['POST'])
def create_record():
    data = request.json
    try:
        validated_data = record_schema.load(data)

        record = Record(**validated_data)
        db.session.add(record)
        db.session.commit()

        return jsonify(record_schema.dump(record)), 201
    
    except ValidationError as e:
        return jsonify({"error": e.messages}), 400


@bp.route('/record/<int:record_id>', methods=['GET'])
def get_record(record_id):
    record = Record.query.get(record_id)
    if not record:
        return jsonify({'error': 'Record not found'}), 404
    return jsonify(record_schema.dump(record))


@bp.route('/record/<int:record_id>', methods=['DELETE'])
def delete_record(record_id):
    record = Record.query.get(record_id)
    if not record:
        return jsonify({'error': 'Record not found'}), 404

    db.session.delete(record)
    db.session.commit()
    return '', 204


@bp.route('/record', methods=['GET'])
def get_records():
    user_id = request.args.get('user_id', type=int)
    category_id = request.args.get('category_id', type=int)

    query = Record.query
    if user_id:
        query = query.filter_by(user_id=user_id)
    if category_id:
        query = query.filter_by(category_id=category_id)

    records = query.all()
    return jsonify(record_schema.dump(records, many=True))

#4 Ендпоінти для валюти
@bp.route('/currency', methods=['GET'])
def get_currency():
    currency = Currency.query.all()
    return jsonify(currency_schema.dump(currency, many=True))


