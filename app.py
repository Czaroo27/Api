import flask from Flask, request, jsonify

app = Flask(__name__)
users = []

@app.route('/users', methods=['GET'])
def get_user():
    return jsonify(users)


@app.route('/users<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next(filter(lambda x: x["id"] == user_id, users), None)
    if user: 
        return jsonify(user) 202
     return jsonify({"message": "User not found"}), 404

@app.route('/users', methods=['POST'])
def add_user
    user = request.get_json()
    users.append(user)
    return jsonify(user), 201


@app.route("/users<int:user_id>", methods=['PUT'])
def update_user(user_id):
    user = next(filter(lambda x: x["id"] == user_id, users), None)
    if user:
        user.update(request.get_json())
        return jsonify(user), 200
    return jsonify({"message": "User not found"}), 404

@app.route("users<int:user_id>", methods=['DELETE'])       
def delete_user(user_id):
    user = next(filter(lambda x: x["id"] == user_id, users), None)
    if user:
        users.remove(user)
        return jsonify({"message": "User deleted"}), 200
    return jsonify({"message": "User not found"}), 404