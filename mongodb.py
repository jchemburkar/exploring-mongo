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


def connect_to_database() -> pymongo.MongoClient:
    """ create connection using UN+PW """
    url = get_db_url()
    client = client = pymongo.MongoClient(url)
    return client

########
# main #
########

def main():
    """ main func """
    connect_to_database()


if __name__ == "__main__":
    main()
