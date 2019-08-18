import sys
import random
import string
sys.path.append('../../')
from apis.config.Config import generateFirebaseObject
from flask import Blueprint, request, jsonify
add_urls = Blueprint('add_urls', __name__)

@add_urls.route('/v1/url/add', methods = ['POST'])
def addUrls():
    firebase = generateFirebaseObject()
    db = firebase.database()
    data = request.get_json()
    if 'secret-key' in request.headers:
        ids = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=7))
        print(ids)
        results = db.child("users").child(ids).set(data)
        print(results)
        return jsonify({
        "response-code":200,
        "url": "https://pointmyurl.ml/" + ids
        })
    else:
        return jsonify({
        "response_code": 400,
        "error_message":"authentiction_failed"
    })


