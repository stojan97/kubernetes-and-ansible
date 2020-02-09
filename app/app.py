import os
import uuid

from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
randomUUID = str(uuid.uuid4())
client = MongoClient('mongodb://mongo')
db = client.fikt

@app.route('/add/1')
def add_student():
    db.student.save({index: "INKI254", firstname:"Stojan", lastname:"Samojlovski"})
    
@app.route('/add/2')
def add_student():
    db.student.save({index: "INKI301", firstname:"Stefan", lastname:"Samojlovski"})

@app.route('/')
def get_students():
    _items = db.student.find()
    items_dir = [items for items in _items]
    items_res = list(map(lambda x: x['index'] + ' ' + x['firstname'], items_dir))

    
    str = "Running on server : " + randomUUID + '\n'
    str += '::: Students:  '
    str += ', '.join(items_res)
    return str

if __name__ == '__main__':
    app.run('0.0.0.0')

#db.student.save({index: "INKI254", firstname:"Stojan", lastname:"Samojlovski"})
