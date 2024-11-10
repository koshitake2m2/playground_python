# How to execute.
# $ python app.py
# or
# $ flask run --debugger --reload --port 8080
#

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config["JSON_SORT_KEYS"] = False
CORS(app)


@app.route('/')
def index():
    response_data = {
        'msg': 'hello world',
    }
    return jsonify(response_data)

'''
curl -X GET -H "Content-Type: application/json" "http://localhost:8080/users?hello=world"
'''
@app.route('/users', methods=['GET'])
def user_list():
    response_data = {
        'data': [
            {'name': 'Alice', 'age': 25},
            {'name': 'Bob', 'age': 30},
        ],
        'request_params': request.args,
    }
    return jsonify(response_data)

'''
curl -X GET -H "Content-Type: application/json" "http://localhost:8080/users/1"
'''
@app.route('/users/<int:user_id>')
def user_detail(user_id=None):
    response_data = {
        'user_id': user_id,
    }
    return jsonify(response_data)

'''
curl -X POST -H "Content-Type: application/json" -d '{"name": "Bob", "age": 30}' http://localhost:8080/users
'''
@app.route('/users', methods=['POST'])
def user_create():
    response_data = {
        'name': request.json.get('name'),
        'hobby': request.json.get('hobby'),
        'request_body': request.json,
    }
    return jsonify(response_data)

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=8080)
