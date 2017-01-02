from pymongo import MongoClient
import pymongo
import csv
import os
import sys
import ast

def save(City,From, To):
    post = collect.find_one({"City":City,"From":From, "To":To})
    if(post is None):
        initpost = {"City":City,"From":From,"To":To,"Count":1}
        post_id = collect.insert_one(initpost).inserted_id
        print post_id
    else:
        collect.update_one({'_id': post["_id"]}, {'$inc': {'Count': 1}})

client = MongoClient('localhost', 27017)
db = client['termproject']
collect = db['airbnb_all']

fileList = ["san_diego","portland","oakland","new_orleans","nashville",
            "montreal","melbourne","manchester","madrid","london","hong_kong","geneva","edinburgh","dublin","denver","chicago","boston","berlin","austin","athens","asheville","antwerp","amsterdam"]
notinList=["washington","vienna","victoria","venice","vancouver","toronto","sydney","seattle","san_francisco","los_angeles","new_york_city","paris"]
datapath = 'D:\\workspace\\DataScience\\TermProject\\airbnb_datasets\\new'
os.chdir(datapath)
if os.getcwd() != datapath:
    print "EEROR: the file path incorrect."
    sys.exit()
print(len(fileList))
for fileName in notinList:
    print(fileName)
    f = open(datapath+'\\'+fileName+".csv", 'r')
    csvCursor = csv.reader(f)
    for row in csvCursor:
        for i in range(0, len(row)-1, +1):
            print("City:"+fileName)
            print("From:"+row[i],"To:"+row[i+1])
            save(fileName,row[i],row[i+1])
            print("------------per_data-------------")
        print("###########per_col##############")
    # f.close()
