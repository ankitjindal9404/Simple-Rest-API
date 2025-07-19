from flask import Flask, jsonify, request

app = Flask(__name__)

# Simple in-memory database
users_db = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"}
]

# GET endpoint to retrieve all users
@app.route('/', methods=['GET'])
def get_users():
    return jsonify(users_db)

# POST endpoint to create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = {
        "id": len(users_db) + 1,
        "name": data['name'],
        "email": data['email']
    }
    users_db.append(new_user)
    return jsonify(new_user), 201

if __name__ == '__main__':
    app.run(debug=True)
