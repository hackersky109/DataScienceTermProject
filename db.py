from pymongo import MongoClient
import pymongo
import csv
import os
import sys



def add(From, To):
    post = collect.find_one({"From":From, "To":To})
    if(post is None):
        initpost = {"From":From,"To":To,"Count":1}
        post_id = collect.insert_one(initpost).inserted_id
        print post_id
    else:
        collect.update_one({'_id': post["_id"]}, {'$inc': {'Count': 1}})
def get(From):
    # for doc in collect.find({"From":From}).sort("Count",pymongo.ASCENDING):
    return collect.find({"From":From}).sort("Count",pymongo.DESCENDING)[0]


client = MongoClient('localhost', 27017)
db = client['termproject']
collect = db['test']

datapath = 'D:\\workspace\\DataScience\\TermProject'
os.chdir(datapath)
if os.getcwd() != datapath:
    print "EEROR: the file path incorrect."
    sys.exit()

f = open(datapath+'\data.csv', 'r')
for row in csv.DictReader(f):
    list = row['path'].split(',')
    for i in range(0, len(list)-1, +1):
        add(list[i],list[i+1])
f.close()






# a = get("Taipei")
# print(a)
