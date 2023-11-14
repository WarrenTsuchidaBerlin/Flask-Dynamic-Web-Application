from flask import Blueprint, render_template, request, jsonify, redirect, url_for
#Initializes Blueprint
views = Blueprint("views", __name__)

#http://127.0.0.1:5000/views/
@views.route("/")
def home():
    return render_template("index.html", name="Warren", age=28)
#http://127.0.0.1:5000/views/profile
@views.route("/profile")
def profile():
    return render_template("profile.html")
#http://127.0.0.1:5000/views/json
@views.route("/json")
def get_json():
    return jsonify({'name': 'tim', 'coolness': 10})
#get data from a route that is incoming via JSON format, so whatever sent will just return
@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)
#redirect to a different page
#http://127.0.0.1:5000/views/go-to-home
@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("views.home"))