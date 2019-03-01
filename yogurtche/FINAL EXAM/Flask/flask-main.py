from flask import Flask, jsonify, render_template
from blueprints.students_blueprint import auth

from flask import Flask  
app = Flask(__name__)    

@app.route('/')   
def main():
    return render_template("home.html")

    
app.register_blueprint(auth, url_prefix='api/v1/auth')