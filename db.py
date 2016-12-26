from pymongo import MongoClient
client = MongoClient('localhost', 27017)

db = client['termproject']
collect = db['test']


def add(From, To):
    post = collect.find_one({"From":From, "To":To})
    if(post is None):
        initpost = {"From":From,"To":To,"Count":1}
        post_id = collect.insert_one(initpost).inserted_id
        print post_id
    else:
        collect.update_one({'_id': post["_id"]}, {'$inc': {'Count': 1}})
