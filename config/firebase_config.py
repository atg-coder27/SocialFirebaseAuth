from firebase_admin import firestore
import pyrebase
from pyrebase.pyrebase import Database

firebaseConfig = {
  "apiKey": "AIzaSyDQym75vbuRjptkNhn8ChxOz59_eUjD2j4",
  "authDomain": "test1-4c5c1.firebaseapp.com",
  "databaseURL": "https://test1-4c5c1-default-rtdb.firebaseio.com",
  "projectId": "test1-4c5c1",
  "storageBucket": "test1-4c5c1.appspot.com",
  "messagingSenderId": "484897139841",
  "appId": "1:484897139841:web:40ce3b00c0378e0f513180",
  "measurementId": "G-FPF8T0DWYE"
}

firebase = pyrebase.initialize_app(firebaseConfig)
firebase_authe = firebase.auth()
firebase_database = firebase.database()
print("Ansh")
