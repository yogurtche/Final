from flask import Blueprint, request, render_template
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy



auth = Blueprint('auth', __name__)

@auth.route("/<int:param>", methods=['GET'])       #GET METHOD                       
def auth_get(param):
    if param == "Test":
        return "Success"
    else:
        return "Fail"


@auth.route("/<int:param>", methods=['POST'])             #POST 
def course_put_post(param):
return param