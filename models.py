from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
from flask_marshmallow import Marshmallow
import secrets

# set variables for class instantiation
ma = Marshmallow()
db = SQLAlchemy()

# May need user class to handle data from authenticator

# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(user_id)

# Create User Class
class User(db.Model):
    uid = db.Column(db.String(150), primary_key=True)
    displayName = db.Column(db.String(200), nullable = True)
    email = db.Column(db.String(150), nullable = False)
    # date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)

    def __init__(self, uid, email, displayName):
        self.uid = uid
        self.displayName = displayName
        self.email = email
    
    def __repr__(self):
        return f'User {self.displayName} has been added to the database.'
    
class UserSchema(ma.Schema):
    class Meta:
        fields = ['uid', 'displayName', 'email']

user_schema = UserSchema()
    
# Create Car class
class Car(db.Model):
    id = db.Column(db.String, primary_key = True)
    year = db.Column(db.String(10))
    make = db.Column(db.String(100))
    model = db.Column(db.String(100))
    color = db.Column(db.String(100))
    # uid = db.Column(db.String, db.ForeignKey('user.uid'), nullable = False)

    def __init__(self, year, make, model, color):
        self.id = self.set_id()
        self.year = year
        self.make = make
        self.model = model
        self.color = color
        # self.uid = uid

    def set_id(self):
        return(secrets.token_urlsafe())
    
class CarSchema(ma.Schema):
    class Meta:
        fields = ['id', 'year', 'make', 'model', 'color']

car_schema = CarSchema()
cars_schema = CarSchema(many=True)

# Create Log class
class Log(db.Model):
    id = db.Column(db.String, primary_key = True)
    service_type =db.Column(db.String(100))
    notes = db.Column(db.String(1000))
    miles = db.Column(db.String(10))
    cost = db.Column(db.String(10))
    mechanic = db.Column(db.String(100))
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    # uid = db.Column(db.String, db.ForeignKey('user.uid'), nullable = False)
    car_id = db.Column(db.String, db.ForeignKey('car.id'), nullable = False)

    def __init__(self, service_type, notes, miles, cost, mechanic, car_id):
        self.id = self.set_id()
        self.service_type = service_type
        self.notes = notes
        self.miles = miles
        self.cost = cost
        self.mechanic = mechanic
        # self.uid = uid
        self.car_id = car_id

    def __repr__(self):
        return f'You successfully added a {self.service_type} to the log.'
    
    def set_id(self):
        return(secrets.token_urlsafe())
    
class LogSchema(ma.Schema):
    class Meta:
        fields = ['id', 'service_type', 'notes', 'miles', 'cost', 'mechanic']
    
log_schema = LogSchema()
logs_schema = LogSchema(many=True)