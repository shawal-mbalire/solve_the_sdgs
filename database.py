import os
import pyrebase
from dotenv import load_dotenv

load_dotenv(".env")
FIRE_API_KEY = os.getenv("FIRE_API_KEY")

config = {
  "apiKey": FIRE_API_KEY,
  "authDomain": "projectId.firebaseapp.com",
  "databaseURL": "https://medicman-a6044-default-rtdb.europe-west1.firebasedatabase.app/",
  "storageBucket": "projectId.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

def insert_user(user): # takes in user dictionary
    """insert_user` inserts a user into the database."""
    db.child("users").push(user)


def fetch_all_users():
    """`fetch_all_users` fetches all users from the database.`"""
    all=[]
    users = db.child("users").get()
    users = users.val()
    for user in users:
        all.append(users[user])
    return all#list of dictionaries

def fetch_user(user):
    """`fetch_user` fetches a user from the database.`"""
    pass

def update_user(username, name, password):
    """`update_user` updates a user in the database.`"""
    pass

def delete_user(username):
    """`delete_user` deletes a user from the database.`"""
    pass

