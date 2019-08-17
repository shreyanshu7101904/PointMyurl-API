import sys
import random
import string
sys.path.append('../../')
from apis.config.Config import generateFirebaseObject
from flask import Blueprint

add_urls = Blueprint('add_urls', __name__)

@add_urls.route('/v1/url/add', methods = ['GET'])
def addUrls():
    firebase = generateFirebaseObject()
    db = firebase.database()
    data = {
        "name": "Mortimer 'Morty' Smith"
    }
    ids = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=7))
    print(ids)
    results = db.child("users").child(ids).set(data)
    print(results)
    return ids


firebase = generateFirebaseObject()
print(firebase)
db = firebase.database()
data = {
    "name": "Mortimer 'Morty' Smith"
}
results = db.child("users").push(data)