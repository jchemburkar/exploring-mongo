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
    document_three = {"_id": 3, "message": "insert many part 1"}
    document_four = {"_id": 4, "message": "insert many part 2"}
    collection.insert_many([document_three, document_four])


##################
# query database #
##################

def query_database_using_filter(collection: pymongo.collection.Collection) -> None:
    """ find a row using simple filters, on _id and on a non-id column """
    print()
    print("Querying DB Using Filter")

    # use a single filter on _id
    document_one = list(collection.find({"_id": 1}))
    if len(document_one) > 0:
        print(f"Found document with _id=1 by id: {document_one}")

    # use a compound filter on non-id fields
    document_two = list(collection.find({"author": "jonathan", "message": "this is a test"}))
    if len(document_two) > 0:
        print(f"Found document with _id=2 by author, message: {document_two}")


def query_database_using_regex(collection: pymongo.collection.Collection) -> None:
    """ we want to find the document with _id=2; use a regex to find is in the message """
    print()
    print("Querying DB Using Regex")
    regex = "^this" # message starts with 'this'
    document_two = list(collection.find({"message": {"$regex": regex}}))
    if len(document_two) > 0:
        print(f"Found document with _id=2 using regex on message: {document_two}")


def query_database_for_missing_field(collection: pymongo.collection.Collection) -> None:
    """ search for rows 3 and 4 by checking for the absence of a author! """
    print()
    print("Querying DB Using Field Exists")
    query = {"author": {"$exists": False}}
    documents = list(collection.find(query))
    if len(documents) > 0:
        print(f"Found the following documents missing authors: {documents}")


########
# main #
########

def main():
    """ main func """
    client = connect_to_database()
    database = get_database(client, "testdb")
    collection = get_collection(database, "testcollection")

    # populate db
    insert_using_insert_one(collection)
    insert_using_insert_many(collection)

    # verify data / try querying methods
    query_database_using_filter(collection)
    query_database_using_regex(collection)
    query_database_for_missing_field(collection)


if __name__ == "__main__":
    main()
