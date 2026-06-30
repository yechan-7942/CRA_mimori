from pymongo import MongoClient
from config.config_cilent import MONGO_URI, MONGO_DB, MONGO_COLLECTION

_client = None

def get_db():
    global _client
    if _client is None:
        _client = MongoClient(MONGO_URI)
    return _client[MONGO_DB]

def get_collection():
    return get_db()[MONGO_COLLECTION]

def close():
    global _client
    if _client:
        _client.close()
        _client = None