import sys
import pyrebase 

sys.path.append('../')
from config.Config import generateFirebaseObject

firebase = generateFirebaseObject()
print(firebase)
db = firebase.database()
data = {
    "name": "Mortimer 'Morty' Smith"
}
results = db.child("users").push(data)