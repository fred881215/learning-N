import pymongo
import os
from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = os.getenv('MONGODB_URI')
MONGODB_DB_NAME = os.getenv('MONGODB_DB_NAME')
DB_ACCOUNT = os.getenv('DB_ACCOUNT')
DB_PW = os.getenv('DB_PW')
DB_MECHANISM = os.getenv('DB_MECHANISM')

client = pymongo.MongoClient(MONGODB_URI)

db = client.MONGODB_DB_NAME

collection = db.students

student1 = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}

student2 = {
    'id': '20170202',
    'name': 'Mike',
    'age': 21,
    'gender': 'male'
}

result1 = collection.insert_one(student1)
print(result1)
print(result1.inserted_id)

# result2 = collection.insert_many([student1,student2])
# print(result2)
# print(result2.inserted_ids)

# # find
# result = collection.find_one({'name': 'Mike'})
# print(type(result))
# print(result)