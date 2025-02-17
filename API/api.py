"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Merhaba Flask!"

if __name__ == '__main__':
    app.run(debug=True)



from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/resource',
methods=['GET'])
def get_resource():
    return jsonify({"message":
"Resource retrieved successfuly"})

if __name__ == '__main__':
    app.run(debug=True)
"""


"""
@app.route('/api/resource',methods=['POST'])
def create_resource():
    data = request.get_json()
    return jsonify({"data":data, "message": "POST request successful"}),201


"""

from flask import Flask, jsonify

app = Flask(__name__)

users = [
    ("id":1, "name":"Oğuzhan","email":"ozifisek@gmail.com"),
    ("id":2, "name":"Oğuzhan","email":"ozifisek@gmail.com")]

@app.route('/users',methods = ['GET'])
def listUsers():
    return jsonify(users)
@app.route('/users',methods = ['POST'])
def add_users():
    new_user = request.json
    if "id" not in new_user or "name" not in new_user or "email" not in new_user:
        return jsonify({"error":"Eksik bilgiler"}),400
    users.append(new_user)
    return jsonify(new_user),201
@app.route("/users/4", methods =["PUT"])
def update_user(user_id):
    for user in users:
        if user["name"]

if __name__ == '__main__':
    app.run(debug=True)


