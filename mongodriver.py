from typing import Collection
import sys

def get_database():
    from pymongo import MongoClient
    import pymongo

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    # CONNECTION_STRING = "localhost:27017"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    from pymongo import MongoClient
    client = MongoClient()

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['test_database']

def get_mongodb_client_remote(url):
    from pymongo import MongoClient
    import pymongo

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    from pymongo import MongoClient
    client = MongoClient(url)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client

def get_mongodb_db(client,dbName):
    return client[dbName]
def get_collection(db,collectionName):
    return db[collectionName]
def insert_data(collection,data):
    collection.insert_many(data)
    return
def search_data(colection,filter):
    return colection.find(filter)
def delete_data(collection,filter):
    collection.delete_many(filter)
    return 

# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":

    # Get the database
    dbname = get_database()
    collection = dbname['test_collection']
    print(dbname)
    print(collection)

    dict = {'name':'pengzhen'}
    collection.insert_one(dict)

    cursor = collection.find({})
    data = [d for d in cursor]
    print(sys.getsizeof(data))
    print(data)

