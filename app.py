from flask import Flask, request, render_template, url_for, jsonify
from flask_pymongo import PyMongo
import datetime


app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'assignment'
app.config['MONGO_URI'] = "mongodb+srv://manoj:Santosh938@cluster0.pyfbt.mongodb.net/assignment?retryWrites=true&w=majority"

mongo = PyMongo(app)

users = mongo.db.assign_api


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/create_user', methods=['POST', 'GET'])
def create_user():
    if request.method == 'POST':
        name = request.form['user_name']
        mobile_no = request.form['mobile_no']
        time_stamp = datetime.datetime.now().timestamp()
        users.insert_one({'name': name, 'mobile_no': mobile_no, 'time_stamp': time_stamp})
        return 'User Created'
    return render_template('create_user.html')


@app.route('/fetch_users', methods=['POST', 'GET'])
def fetch_users():
    dic = []
    for i in users.find({}, {'_id': False}):
        dic.append(i)
    return jsonify(dic)


if __name__ == "__main__":
    app.run(debug=True)



