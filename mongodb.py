""" test connecting to database """
import json
import pymongo

#######################
# database connection #
#######################

def get_db_url() -> str:
    """ gets database url formatted with password """
    data = json.loads(open("credentials.json").read())
    url = f"mongodb+srv://{data['USERNAME']}:{data['PASSWORD']}@cluster0.aysmmbq.mongodb.net/?retryWrites=true&w=majority"
    return url


def connect_to_database() -> pymongo.mongo_client.MongoClient:
    """ create connection using UN+PW """
    url = get_db_url()
    client = client = pymongo.MongoClient(url)
    return client


########################################
# database creation + insert test data #
########################################

def get_database(client: pymongo.mongo_client.MongoClient, database_name: str) -> pymongo.database.Database:
    """ use the client to call on a database -- it will create it if it doesnt exist! """
    database = client[database_name]
    return database


def get_collection(database: pymongo.database.Database, collection_name: str) -> pymongo.collection.Collection:
    """ use the client to get a collection -- it will create it if it doesnt exist! """
    collection = database[collection_name]
    return collection


def insert_using_insert_one(collection: pymongo.collection.Collection) -> None:
    """ create two sample rows by using insert one """
    document_one = {"_id": 1, "message": "hello world", "author": "jchem"}
    document_two = {"_id": 2, "message": "this is a test", "author": "jonathan"}
    collection.insert_one(document_one)
    collection.insert_one(document_two)


def insert_using_insert_many(collection: pymongo.collection.Collection) -> None:
    """ create two sample rows by using insert many """
    document_one = {"_id": 3, "message": "insert many part 1"}
    document_two = {"_id": 4, "message": "insert many part 2"}
    collection.insert_many([document_one, document_two])


########
# main #
########

def main():
    """ main func """
    client = connect_to_database()
    database = get_database(client, "testdb")
    collection = get_collection(database, "testcollection")
    insert_using_insert_many(collection)


if __name__ == "__main__":
    main()
