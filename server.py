from sqlite3 import Connection as SQLite3Connection
from datetime import datetime
from sqlalchemy import event
from sqlalchemy.engine import Engine
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from BinarySearchTree.binary_search_tree import BinarySearchTree
from HashMap.hash_map import HashTable
from LinkedList import linked_list
import random

from Queue.queue import Queue
from Stack.stack import Stack


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
    data = request.get_json()
    user = User.query.filter_by(id=user_id).first()
    if not user:
        return jsonify({"error": "no user exists with given user_id"}), 400
    # TODO: static table size has to be user based
    ht = HashTable(10)
    ht.add_key_value_pair("title",data["title"])
    ht.add_key_value_pair("body", data["body"])
    ht.add_key_value_pair("date",now)
    ht.add_key_value_pair("user_id",user_id)
    """
        for visualization purpose only
        in the terminal view
    """
    ht.print_table()
    new_blog = BlogPost(
        title = ht.get_value("title"),
        body = ht.get_value("body"),
        date = ht.get_value("date"),
        user_id = ht.get_value("user_id")
    )
    db.session.add(new_blog)
    db.session.commit()
    return jsonify({"message": "New blog post created"}), 201
    

@app.route("/blog_post/<blog_post_id>", methods=["GET"])
def get_one_blog_post(blog_post_id):
    blog_posts = BlogPost.query.all() # default order is accending
    """
        NOTE: as the default order is accending while inserting
        data into bst it will the tree unbalanced which will lead to
        linear order of search
    """
    # HACK: randomize the order before insert this will result in constructing a balanced bst
    random.shuffle(blog_posts)
    bst = BinarySearchTree()
    for post in blog_posts:
        bst.insert({
            "id": post.id,
            "title": post.title,
            "body": post.body,
            "user_id": post.user_id
        })
    target_post = bst.search(blog_post_id)
    if not target_post:
        return jsonify({"error": "post not found"}), 400
    
    return jsonify({"message": "post found", "data":target_post})
    

@app.route("/blog_post/numeric_body", methods=["GET"])
def get_numeric_post_bodies():
    custom_queue = Queue()
    numeric_data_list = []
    blogs = BlogPost.query.all()
    for blog in blogs:
        custom_queue.enqueue(blog)
    for _ in range(len(blogs)):
        post = custom_queue.dequeue()
        numeric_body = 0
        for char in post.data.body:
            numeric_body += ord(char)
        post.data.body = numeric_body
        numeric_data_list.append({
            "id": post.data.id,
            "title": post.data.title,
            "body": post.data.body,
            "user_id": post.data.user_id
        })
    
    return jsonify(numeric_data_list)
            

@app.route("/blog_post/delete_last_n_posts/<n>", methods=["DELETE"])
def delete_last_n_posts(n):
    custom_stack = Stack()
    blogs = BlogPost.query.all()
    for post in blogs:
        custom_stack.push(post)
    for _ in range(n):
        deleted_post = custom_stack.pop()
        db.session.delete(deleted_post)
        db.session.commit()
    return jsonify({"message": "successfully deleted posts"})
        

if __name__ == "__main__":
    app.run(host="127.0.0.1",debug=True,port=5555)