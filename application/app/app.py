import os
from flask import Flask
from pymongo import MongoClient


config = {
    "port": os.environ.get('PORT', 5000),
    "debug": os.environ.get('DEBUG', False),
    "mongohost": os.environ.get('MONGOHOST', 'mongo'),
    "mongoport": os.environ.get('MONGOPORT', 27017),
    "useraccount": os.environ.get('USERACCOUNT', 'root'),
    "userpasswd": os.environ.get('USERPASSWD', 'example'),
    "mongodb": os.environ.get('MONGODB', 'akopytsiadb'),
    "andriicollect": os.environ.get('ANDRIICOLLECT', 'andriicollect')
}

app = Flask(__name__)
client = MongoClient(config["mongohost"], config["mongoport"], username=config["useraccount"], password=config["userpasswd"])


@app.route("/")
def hello():
    return "Hello, Python!"


@app.route("/check")
def check():
    try:
        client.admin.command('ismaster')
    except:
        return "Server not available"
    return "Hello from the MongoDB client!\n"

@app.route("/read/")
def read():
    acts = []
    db = client[config["mongodb"]]
    collection = db[config["andriicollect"]]
    for act in collection.find({},{ "_id": 0, "name": 1, "type": 1 }):
        acts.append(act)
    return repr(acts)


@app.route("/write/")
def write():
    db = client[config["mongodb"]]
    collection = db[config["andriicollect"]]
    mydict = { "name": "Easy2", "type": "AmazonCloud" }
    x = collection.insert_one(mydict)
    return repr(x.inserted_id)


@app.route("/find/<int:id>",methods=['POST', 'GET'])
def find(id):
    acts = []
    db = client[config["mongodb"]]
    collection = db[config["andriicollect"]]
    myquery = { "id": id }
    mydoc = collection.find(myquery)
    for act in mydoc:
        acts.append(act)
    return repr(acts)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config["port"], debug=config["debug"])
