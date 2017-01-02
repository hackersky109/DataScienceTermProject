from pymongo import MongoClient
import pymongo
import csv
import os
import sys
import ast



def save(From, To):
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
collect = db['triphobo_all']
fileList = ["washington","vienna","victoria","venice","vancouver","toronto","sydney","seattle","san_francisco","san_diego","portland","paris","oakland","new_york_city","new_orleans","nashville",
            "montreal","melbourne","manchester","madrid","los_angeles","london","hong_kong","geneva","edinburgh","dublin","denver","chicago","boston","berlin","austin","athens","asheville","antwerp","amsterdam"]

datapath = 'D:\\workspace\\DataScience\\TermProject\\triphobo_datasets'
os.chdir(datapath)
if os.getcwd() != datapath:
    print "EEROR: the file path incorrect."
    sys.exit()
print(len(fileList))
for fileName in fileList:
    f = open(datapath+'\\'+fileName+".csv", 'r')
    for row in csv.DictReader(f):
        if isinstance(row['trip_path_detail'], str):
            arr = ast.literal_eval(row['trip_path_detail'])
            for i in arr:
                for j in range(0, len(i)-1, +1):
                    print("City:"+fileName)
                    print("From:"+i[j],"To:"+i[j+1])
                    save(i[j],i[j+1])
                    print('=================')
#     list = row['trip_path_detail'].split(',')
#     for i in range(0, len(list)-1, +1):
#         print(list[i].translate(None,'[]'))
#         print(list[i+1].translate(None,'[]'))
#         print(list[i].translate(None,'[]').split("u'")[1].split("'")[0],list[i+1].translate(None,'[]').split("u'")[1].split("'")[0])
#         save(list[i].translate(None,'[]').split("u'")[1].split("'")[0],list[i+1].translate(None,'[]').split("u'")[1].split("'")[0])
# f.close()

# file = open(datapath + '\washington.csv', 'r')
# csvCursor = csv.reader(file)
# for row in csvCursor:
#     print(row)
#     print(len(row))
#     print("@@@@@@@@@@@@@@@@@@@@@@@@@@")
# file.close()






# a = get("Taipei")
# print(a)
