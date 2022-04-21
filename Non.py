import pymongo
from pymongo import MongoClient

import gridfs 
from gridfs import GridFS


client = pymongo.MongoClient("mongodb+srv://Mario:Luigi@floodhunter.bl1w5.mongodb.net/FloodHunter?retryWrites=true&w=majority")


db = client.FloodHunter
collection = db['Submits'] 

