import pymongo
from pymongo import MongoClient

import gridfs 
from gridfs import GridFS

client = pymongo.MongoClient("mongodb+srv://Mario:Luigi@floodhunter.bl1w5.mongodb.net/FloodHunter?retryWrites=true&w=majority")


db = client.FloodHunter
collection = db['Submits'] 



def datastock(title, selftext, url, score, num_comments):
    collection.insert_one(
    {
    "title" : title,
    "selftext" : selftext,
    "url" : url,
    "score" : score,
    "num_comments" : num_comments
    })


   
def resetcollection():
    collection.delete_many({}) 



resetcollection()

fs = gridfs.GridFS(db)




#Video1 ===================================================================================================================

#define an video object with the location.
filev = "./Videos_Eric/Po-2013/video1.mp4"
#Open the video in read-only format.
with open(filev, 'rb') as f:
    contentsv = f.read()
#Now store/put the video via GridFs object.
fs.put(contentsv, filename="file")

#define an image object with the location.
filei = "./Videos_Eric/Po-2013/Image1.JPG"
#Open the image in read-only format.
with open(filei, 'rb') as f:
    contentsi = f.read()
#Now store/put the image via GridFs object.
fs.put(contentsi, filename="file")

collection.insert_one(
    {
    "Date" : "18/06/2013",
    "Username" : "Amogus",
    "Latitude" : 43.2951,
    "Longitude" : -0.3708,
    "Image" : contentsi,
    "Video" : contentsv,
    })





# Video2 ======================================================================

#define an video object with the location.
filev = "./Videos_Eric/Po-2013/video2.mp4"
#Open the video in read-only format.
with open(filev, 'rb') as f:
    contentsv = f.read()
#Now store/put the video via GridFs object.
fs.put(contentsv, filename="file")

#define an image object with the location.
filei = "./Videos_Eric/Po-2013/Image2.JPG"
#Open the image in read-only format.
with open(filei, 'rb') as f:
    contentsi = f.read()
#Now store/put the image via GridFs object.
fs.put(contentsi, filename="file")

collection.insert_one(
    {
    "Date" : "18/06/2013",
    "Username" : "Amogus",
    "Latitude" : 43.2851,
    "Longitude" : -0.3708,
    "Image" : contentsi,
    "Video" : contentsv,
    })





# Video3 ======================================================================


# #define an video object with the location.
# filev = "./Videos_Eric/Po-2013/video3.mp4"
# #Open the video in read-only format.
# with open(filev, 'rb') as f:
#     contentsv = f.read()
# #Now store/put the video via GridFs object.
# fs.put(contentsv, filename="file")

# #define an image object with the location.
# filei = "./Videos_Eric/Po-2013/Image3.JPG"
# #Open the image in read-only format.
# with open(filei, 'rb') as f:
#     contentsi = f.read()
# #Now store/put the image via GridFs object.
# fs.put(contentsi, filename="file")

# collection.insert_one(
#     {
#     "Date" : "18/06/2013",
#     "Username" : "Amogus",
#     "Latitude" : 42.8735,
#     "Longitude" : -0.0029,
#     "Image" : contentsi,
#     "Video" : contentsv,
#     })





# Video4 ======================================================================

#define an video object with the location.
filev = "./Videos_Eric/Po-2013/video4.mp4"
#Open the video in read-only format.
with open(filev, 'rb') as f:
    contentsv = f.read()
#Now store/put the video via GridFs object.
fs.put(contentsv, filename="file")

#define an image object with the location.
filei = "./Videos_Eric/Po-2013/Image4.JPG"
#Open the image in read-only format.
with open(filei, 'rb') as f:
    contentsi = f.read()
#Now store/put the image via GridFs object.
fs.put(contentsi, filename="file")



collection.insert_one(
    {
    "Date" : "18/06/2013",
    "Username" : "Amogus",
    "Latitude" : 43.3951,
    "Longitude" : -0.308,
    "Image" : contentsi,
    "Video" : contentsv,
    })





# Video5 / 2nd folder ======================================================================

#define an video object with the location.
filev = "./Videos_Eric/Sicile-2011/Video5.mp4"
#Open the video in read-only format.
with open(filev, 'rb') as f:
    contentsv = f.read()
#Now store/put the video via GridFs object.
fs.put(contentsv, filename="file")

#define an image object with the location.
filei = "./Videos_Eric/Sicile-2011/Image5.JPG"
#Open the image in read-only format.
with open(filei, 'rb') as f:
    contentsi = f.read()
#Now store/put the image via GridFs object.
fs.put(contentsi, filename="file")



collection.insert_one(
    {
    "Date" : "22/11/2011",
    "Username" : "Amogus",
    "Latitude" : 41.3874,
    "Longitude" : 2.1686,
    "Image" : contentsi,
    "Video" : contentsv,
    })





# Video6 ======================================================================

#define an video object with the location.
filev = "./Videos_Eric/Sicile-2011/Video6.mp4"
#Open the video in read-only format.
with open(filev, 'rb') as f:
    contentsv = f.read()
#Now store/put the video via GridFs object.
fs.put(contentsv, filename="file")

#define an image object with the location.
filei = "./Videos_Eric/Sicile-2011/Image6.JPG"
#Open the image in read-only format.
with open(filei, 'rb') as f:
    contentsi = f.read()
#Now store/put the image via GridFs object.
fs.put(contentsi, filename="file")



collection.insert_one(
    {
    "Date" : "22/11/2011",
    "Username" : "Amogus",
    "Latitude" : 41.3774,
    "Longitude" : 2.1586,
    "Image" : contentsi,
    "Video" : contentsv,
    })





# Video7 ======================================================================


# 10 min trop long

# #define an video object with the location.
# filev = "./Videos_Eric/Sicile-2011/Video7.mp4"
# #Open the video in read-only format.
# with open(filev, 'rb') as f:
#     contentsv = f.read()
# #Now store/put the video via GridFs object.
# fs.put(contentsv, filename="file")

# #define an image object with the location.
# filei = "./Videos_Eric/Sicile-2011/Image7.JPG"
# #Open the image in read-only format.
# with open(filei, 'rb') as f:
#     contentsi = f.read()
# #Now store/put the image via GridFs object.
# fs.put(contentsi, filename="file")



# collection.insert_one(
#     {
#     "Date" : "22/11/2011",
#     "Username" : "Amogus",
#     "Latitude" : 41.3274,
#     "Longitude" : 2.1286,
#     "Image" : contentsi,
#     "Video" : contentsv,
#     })







#datastock("title", "selftext", "url", 5, 10)


# collection.insert_one(
#     {
#     "title" : "title",
#     "selftext" : "selftext",
#     "url" : "url",
#     "score" : 10,
#     "num_comments" : 10
#     })