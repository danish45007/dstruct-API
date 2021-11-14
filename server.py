from sqlite3 import Connection as SQLite3Connection
from datetime import datetime
from sqlalchemy import event
from sqlalchemy.engine import Engine
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from LinkedList import linked_list

# main app
app = Flask(__name__)

# database configs
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlitedb.file"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = 0

# config sqlite to enforce foreign key contraints
@event.listens_for(Engine, "connect")
def _set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, SQLite3Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON;")
        cursor.close()

# init sqlite database
db = SQLAlchemy(app)
now = datetime.now()

# models
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    address = db.Column(db.String(200))
    phone = db.Column(db.String(50))
    posts = db.relationship("BlogPost", cascade="all, delete")


class BlogPost(db.Model):
    __tablename__ = "blog_post"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    body = db.Column(db.String(200))
    date = db.Column(db.Date)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)


# routes
@app.route("/user", methods=["POST"])
def create_user():
    data = request.get_json()
    new_user = User(
        name=data["name"],
        email=data["email"],
        address=data["address"],
        phone=data["phone"],
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created"}), 201


@app.route("/user/descending_id", methods=["GET"])
def get_all_users_descending():
    users = User.query.all()
    all_user_ll = linked_list.LinkedList()
    for user in users:
        all_user_ll.insert_beginning({
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "address": user.address,
            "phone": user.phone
        })
    return jsonify({"users": all_user_ll.to_list()}), 200
    


@app.route("/user/ascending_id", methods=["GET"])
def get_all_users_ascending():
    users = User.query.all()
    all_user_ll = linked_list.LinkedList()
    for user in users:
        all_user_ll.insert_beginning({
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "address": user.address,
            "phone": user.phone
        })
    return jsonify({"users": all_user_ll.to_list()}), 200
    


@app.route("/user/<user_id>", methods=["GET"])
def get_one_user(user_id):
    users = User.query.all()
    all_user_ll = linked_list.LinkedList()
    for user in users:
        all_user_ll.insert_beginning({
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "address": user.address,
            "phone": user.phone
        })
    required_user = all_user_ll.get_node_by_id(user_id)
    if required_user == None:
        return jsonify({"msg": "No user exists with the passed user_id"}), 400
    return jsonify({"user": required_user}), 200


@app.route("/user/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    db.session.delete(user)
    db.session.commit()
    return jsonify({"msg": f"user with id {user_id} deleted successfully"}), 200
    
    
@app.route("/blog_post/<user_id>", methods=["POST"])
def create_blog_post(user_id):
    pass

@app.route("/blog_post/<blog_post_id>", methods=["GET"])
def get_one_blog_post(blog_post_id):
    pass

@app.route("/blog_post/numeric_body", methods=["GET"])
def get_numeric_post_bodies():
    pass

@app.route("/blog_post/delete_last_10", methods=["DELETE"])
def delete_last_10():
    pass

if __name__ == "__main__":
    app.run(debug=True)