from pymongo import MongoClient
client = MongoClient('localhost', 27017)

db = client['termproject']
collect = db['test']


From = "Taipei"
To = "Ilan"
post = collect.find_one({"From":From, "To":To})
if(post is None):
    initpost = {"From":From,"To":To,"Count":"1"}
    post_id = collect.insert_one(post).inserted_id
    print post_id
else:
    count = post
    print(post)
