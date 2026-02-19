import os
import redis


def get_conn_to_redis():
    # env's
    REDIS_HOST = os.getenv("REDIS_HOST", "localhost")

    ## redis
    CONF_REDIS =  {"host":REDIS_HOST, "port":6379,"decode_responses":True}
    redis_client = redis.Redis(**CONF_REDIS)

    return redis_client

