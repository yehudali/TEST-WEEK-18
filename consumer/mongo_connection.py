import os
from pymongo import MongoClient



def get_conn_to_mongo():
    
    ## env's:
    MONGO_URL = os.getenv('MONGO_URL', "mongodb://root:root123@localhost:27017/")

    ## MONGO 
    claient = MongoClient(MONGO_URL)
    db = claient['db']
    coll = db['alerts']

    return coll, claient