from flask import Blueprint

from .extensions import mongo

main = Blueprint('main', __name__)


@main.route('/')
def index():
    user_collection = mongo.db.usersNew
    user_collection.insert({'name' : 'Anthony'})
    return '<h1>User added succesfully!</h1>'