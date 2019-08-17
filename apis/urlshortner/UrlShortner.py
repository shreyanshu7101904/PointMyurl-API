import sys
sys.path.append('../')
from config.Config import generateFirebaseObject

add_urls = Blueprint('add_urls', __name__)

@add_urls.route('/v1/url/add', methods = ['POST'])
def addUrls():
    firebase = generateFirebaseObject()
    db = firebase.database()
    data = {
        "name": "Mortimer 'Morty' Smith"
    }
    results = db.child("users").push(data)
    return resu.status


firebase = generateFirebaseObject()
print(firebase)
db = firebase.database()
data = {
    "name": "Mortimer 'Morty' Smith"
}
results = db.child("users").push(data)