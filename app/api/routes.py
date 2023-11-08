from flask import Blueprint, request, jsonify
from helpers import token_required
from models import db, Car, car_schema, cars_schema, Log, log_schema, logs_schema, User, user_schema

api = Blueprint('api', __name__, url_prefix='/api')

# Create User route
@api.route('/users', methods = ['POST'])

def create_user():
    uid = request.json['uid']
    displayName = request.json['displayName']
    email = request.json['email']

    user = User(uid, displayName, email)

    db.session.add(user)
    db.session.commit()

    response = user_schema.dump(user)
    return jsonify(response)

# Create Car route
@api.route('/cars', methods = ['POST'])
# @token_required

def create_car():
    year = request.json['year']
    make = request.json['make']
    model = request.json['model']
    color = request.json['color']
    # uid = request.json['uid']

    car = Car(year, make, model, color)

    db.session.add(car)
    db.session.commit()

    response = car_schema.dump(car)
    return jsonify(response)

# Route to get all cars in inventory
@api.route('/cars', methods = ['GET'])
# @token_required
def get_cars():
    # the_user = uid.token
    # cars = Car.query.filter_by(uid = the_user).all()
    cars = Car.query.all()
    response = cars_schema.dump(cars)
    return jsonify(response)

# Route to get single car in inventory
@api.route('/cars/<carid>', methods = ['GET'])
# @token_required
def get_single_car(carid):
    car = Car.query.get(carid)
    response = car_schema.dump(car)
    return jsonify(response)

# Update car route
@api.route('/cars/<carid>', methods = ['POST'])
# @token_required
def update_car(carid):
    car = Car.query.get(carid)
    car.year = request.json['year']
    car.make = request.json['make']
    car.model = request.json['model']
    car.color = request.json['color']
    # car.uid = uid.token

    db.session.commit()
    response = car_schema.dump(car)
    return jsonify(response)

# Delete car route
@api.route('/cars/<carid>', methods = ['DELETE'])
# @token_required
def delete_car(carid):
    car = Car.query.get(carid)
    db.session.delete(car)
    db.session.commit()
    response = car_schema.dump(car)
    return jsonify(response)

# Create log route
@api.route('/cars/<carid>/logs', methods = ['POST'])
# @token_required

def create_log(carid):
    service_type = request.json['service_type']
    notes = request.json['notes']
    miles = request.json['miles']
    cost = request.json['cost']
    mechanic = request.json['mechanic']
    car_id = carid

    print(f'log maker: {car_id}')

    log = Log(service_type, notes, miles, cost, mechanic, car_id)

    db.session.add(log)
    db.session.commit()

    response = log_schema.dump(log)
    return jsonify(response)

# Route to get all service logs for a particular car
@api.route('/cars/<carid>/logs', methods = ['GET'])
# @token_required
def get_logs(carid):
    a_car = carid
    logs = Log.query.filter_by(car_id = a_car).all()
    # logs = Log.query.all()
    response = logs_schema.dump(logs)
    return jsonify(response)

# Route to get a single service log
@api.route('/cars/<carid>/logs/<logid>', methods = ['GET'])
# @token_required
def get_single_log(carid, logid):
    log = Log.query.get(logid)
    response = log_schema.dump(log)
    return jsonify(response)

# Update log route
@api.route('/cars/<carid>/logs/<logid>', methods = ['POST'])
# @token_required
def update_log(carid, logid):
    log = Log.query.get(logid)
    log.service_type = request.json['service_type']
    log.notes = request.json['notes']
    log.miles = request.json['miles']
    log.cost = request.json['cost']
    log.mechanic = request.json['mechanic']
    # log.uid = uid.token

    db.session.commit()
    response = log_schema.dump(log)
    return jsonify(response)

# Delete log route
@api.route('/cars/<carid>/logs/<logid>', methods = ['DELETE'])
# @token_required
def delete_log(carid, logid):
    log = Log.query.get(logid)

    db.session.delete(log)

    db.session.commit()
    response = log_schema.dump(log)
    return jsonify(response)
