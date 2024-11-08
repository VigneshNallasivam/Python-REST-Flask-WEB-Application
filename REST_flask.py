from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

#Instance creation for flask
app = Flask(__name__)

# Configure PostgreSQL URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5433/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Define a model for a resource (e.g., User)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"<User {self.name}>"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }

# Create tables before running the app
def create_tables():
    with app.app_context():
        db.create_all()

# Call create_tables function to ensure tables are created
create_tables()

# Welcoming Page
@app.route('/')
def home():
    return "<h1><b>Welcome to the User API..!!</b></h1>"

### REST Methods Implementation

# 1. GET: Retrieve resources (list or single)
@app.route('/users', methods=['GET'])
def get_users(): 
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user.to_dict())

# 2. POST: Create a new resource
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(name=data['name'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 201

# 3. PUT: Update a resource (full update)
@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    user = User.query.get_or_404(id)
    user.name = data['name']
    user.email = data['email']
    db.session.commit()
    return jsonify(user.to_dict())

# 4. PATCH: Partially update a resource
@app.route('/users/<int:id>', methods=['PATCH'])
def patch_user(id):
    data = request.get_json()
    user = User.query.get_or_404(id)
    if 'name' in data:
        user.name = data['name']
    if 'email' in data:
        user.email = data['email']
    db.session.commit()
    return jsonify(user.to_dict())

# 5. DELETE: Delete a resource
@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted successfully"}), 200

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
