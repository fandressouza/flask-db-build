from flask import Blueprint, jsonify

from .extensions import mongo

main = Blueprint('main', __name__)


@main.route('/insert-many')
def index():
    user_collection = mongo.db.usersNew
    # user_collection.createIndex( {'name' : 1} , {'unique' : True} )
    users = [
        {
            'name' : 'Anthony',
            'email' : 'tony@email.com',
            'age'  : 24,
            'profession' : 'Software Engineer',
            'country' : 'US'
        },
        {
            'name' : 'Mark',
            'email' : 'mark@email.com',
            'age'  : 44,
            'profession' : 'Sales person',
            'country' : 'CA'
        },
        {
            'name' : 'Agatha',
            'email' : 'agatha@email.com',
            'age'  : 27,
            'profession' : 'Dentist',
            'country' : 'FR'
        },
    ]
    user_collection.insert_many(users)
    return '<h1>Users added succesfully!</h1>'


@main.route('/insert-unique')
def insert():
    user_collection = mongo.db.usersNew

    try:

        user_collection.create_index([("email", 1)], unique=True)

        new_user = {
            'name': 'Felipe', 
            'email' : 'felipe@email.com',
            'age': 34,
            'profession': 'Software Developer',
            'country': 'BR'
        }

        user_collection.insert_one(new_user)

        return '<h1>User successfully inserted!</h1>'
        
    except:

        return '<h1>data point already exists</h1>'
    


@main.route('/read-all')
def read():
    user_collection = mongo.db.usersNew
    users = user_collection.find()
    output = [
        {
        'name': user['name'], 
        'email' : user['email'],
        'age': user['age'],
        'profession': user['profession'],
        'country': user['country']
        } for user in users
    ]
    
    return jsonify(output)