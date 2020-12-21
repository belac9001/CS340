from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        self.client = MongoClient('mongodb://%s:%s@localhost:50498' % (username, password))
        self.database = self.client['AAC'] 
        self.animals = self.database['animals'] # collection

    # Insert data into animals collection
    # param: key/value dict
    def create(self, data):
        if isinstance(data, dict):
            if len(data) < 1:
                print("Data is empty")
            elif len(data) > 1:
                self.animals.insert_many(data)
                print("Data inserted successfully")
            else:
                self.animals.insert_one(data)
                print("Data inserted successfully")
        else:
            raise Exception("Nothing to save, data parameter is empty")
    
    # Query and print data from animals collection
    # param: key/value dict
    def read(self, data):
        if isinstance(data, dict):
            found_data = self.animals.find(data)
            
            if found_data.count() == 0:
                print("No data found")
            else:
                for item in found_data:
                    print(item)
        else:
            raise Exception("Incorrect Data Format, must be dictionary")

