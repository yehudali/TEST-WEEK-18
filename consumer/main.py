import json

from mongo_connection import get_conn_to_mongo
from redis_connection import get_conn_to_redis
import uuid
import json
import os
import redis

def run():
    try:
        redis_client = get_conn_to_redis()
        mongo_coll, claient = get_conn_to_mongo()


        # env's
        REDIS_HOST = os.getenv("REDIS_HOST", "localhost")

        ## redis
        CONF_REDIS =  {"host":REDIS_HOST, "port":6379,"decode_responses":True}
        redis_client = redis.Redis(**CONF_REDIS)

        while True:

            repo = redis_client.lpop(name="queue_urgent")
         
            if repo:
                repo = str(repo)
                repo = json.loads(repo)
                repo["time_insertion"] = uuid.uuid4()
                mongo_coll.insert_one(repo)
                continue
                


            else:
                repo = redis_client.lpop(name="queue_normal")
                repo = str(repo)
                repo = json.loads(repo)
                repo["time_insertion"] = uuid.uuid4()

                mongo_coll.insert_one(repo)
                continue
            











        claient.close()
    except Exception as e:
        print(e)
    
    # finally:
    #     claient.close()
        

    




if __name__ == "__main__":
    run()