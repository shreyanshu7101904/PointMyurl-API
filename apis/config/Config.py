import pyrebase 

def generateFirebaseObject():
    config = {
    "apiKey": "AIzaSyCKH6XV8YBfKvRME43F3kqiTkFZELu5yGE",
    "authDomain": "pointmyurl.firebaseapp.com",
    "databaseURL": "https://pointmyurl.firebaseio.com/",
    "storageBucket": "pointmyurl.appspot.com"
    }
    firebase_object = pyrebase.initialize_app(config)
    print(firebase_object)
    return firebase_object


if __name__ == '__main__':
    generateFirebaseObject()