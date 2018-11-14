from pymongo import MongoClient
import datetime
import pprint
client = MongoClient('localhost',
                    port=27020,
                    username='test-user',
                    password='test-password',
                    authSource='admin',
                    authMechanism='SCRAM-SHA-256')

post = {"author": "Nick",
         "text": "My first blog post!",
         "tags": ["mongodb", "python", "pymongo"],
         "date": datetime.datetime.utcnow()}

db = client.taggingtool
posts = db.posts
post_id = posts.insert_one(post).inserted_id
# print(post_id)
#
# pprint.pprint(posts.find_one())

# pprint.pprint(posts.find_one({"_id": post_id}))
for post in posts.find({"author": "Nick"}):
    pprint.pprint(post)
