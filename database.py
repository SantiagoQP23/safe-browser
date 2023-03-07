
#mongodb_cnn = "mongodb+srv://<username>:<password>@miclustercafe.1rxey.mongodb.net/test"
import pymongo
from pymongo import MongoClient

mongodb_cnn = "mongodb+srv://user_python:fbhXsvaHMMGLSNiX@miclustercafe.1rxey.mongodb.net/packetsdb"

client = pymongo.MongoClient(mongodb_cnn)

class CaptureService: 
    def __init__(self):
        self.client = MongoClient(mongodb_cnn)
        try:
            db_list = self.client.list_database_names()
           
        except Exception as e:
            print("Error al conectar a la base de datos:", e)
        self.db = self.client["packetsdb"]
        self.collection = self.db["capture"]

    def insert(self, data):
        result = self.collection.insert_one(data)
        return result.inserted_id

    def find(self, query):
        return self.collection.find(query)
    
    def count(self, query):
        return self.collection.count_documents(query)
    

    def delete(self, query):
        result = self.collection.delete_one(query)
        return result.deleted_count

class DestinationIPService: 
    def __init__(self):
        self.client = MongoClient(mongodb_cnn)
        try:
            db_list = self.client.list_database_names()
            
        except Exception as e:
            print("Error al conectar a la base de datos:", e)
        self.db = self.client["packetsdb"]
        self.collection = self.db["destination_ip"]

    def insert(self, data):
        result = self.collection.insert_one(data)
        return result.inserted_id

    def find(self, query):
        return self.collection.find(query)
    
    def count(self, query):
        return self.collection.count_documents(query)
    
    def find_one(self, query):
        return self.collection.find_one(query)

    def delete(self, query):
        result = self.collection.delete_one(query)
        return result.deleted_count

class IPAnalysisService: 
    def __init__(self):
        self.client = MongoClient(mongodb_cnn)
        try:
            db_list = self.client.list_database_names()
            
        except Exception as e:
            print("Error al conectar a la base de datos:", e)
        self.db = self.client["packetsdb"]
        self.collection = self.db["ip_analysis"]

    def insert(self, data):
        result = self.collection.insert_one(data)
        return result.inserted_id
    
    def count(self, query):
        return self.collection.count_documents(query)

    def find(self, query):
        return self.collection.find(query)
    
    def find_one(self, query):
        return self.collection.find_one(query)

    def delete(self, query):
        result = self.collection.delete_one(query)
        return result.deleted_count


class ConfigService():
    def __init__(self):
        self.client = MongoClient(mongodb_cnn)
        try:
            db_list = self.client.list_database_names()
            
        except Exception as e:
            print("Error al conectar a la base de datos:", e)
        self.db = self.client["packetsdb"]
        self.collection = self.db["config"]

    def insert(self, data):
        result = self.collection.insert_one(data)
        return result.inserted_id
    
    def count(self, query):
        return self.collection.count_documents(query)

    def find(self, query):
        return self.collection.find(query)
    
    def find_one(self, query):
        return self.collection.find_one(query)
    
    def update(self, query, data):
        result = self.collection.update_one(query, data)
        return result.modified_count

    def delete(self, query):
        result = self.collection.delete_one(query)
        return result.deleted_count
