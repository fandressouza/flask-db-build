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
            'age'  : 24,
            'profession' : 'Software Engineer',
            'country' : 'US'
        },
        {
            'name' : 'Mark',
            'age'  : 44,
            'profession' : 'Sales person',
            'country' : 'CA'
        },
        {
            'name' : 'Agatha',
            'age'  : 27,
            'profession' : 'Dentist',
            'country' : 'FR'
        },
    ]
    user_collection.insert_many(users)
    return '<h1>User added succesfully!</h1>'



@main.route('/read-all')
def read():
    user_collection = mongo.db.usersNew
    users = user_collection.find()
    output = [
        {
        'name': user['name'], 
        'age': user['age'],
        'profession': user['profession'],
        'country': user['country']
        } for user in users
    ]
    
    return jsonify(output)