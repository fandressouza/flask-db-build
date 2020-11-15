from flask import Blueprint, jsonify, render_template

from .extensions import mongo

auth = Blueprint('auth', __name__)


@auth.route('/auth/register')
def register():
    return "Welcome to the registration page"

