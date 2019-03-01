from flask import Flask, Response


app = Flask('auth', __name__)


@app.route("/api/v1/auth")
def lair():
    return Response('Final Exam')


@app.route("/api/v1/auth")
def landing_page():
    return Response("Final, final, final!")
    