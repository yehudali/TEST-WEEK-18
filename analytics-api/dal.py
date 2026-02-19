from mongo_connection import get_conn_to_mongo
from redis_connection import get_conn_to_redis
import json

redis_client = get_conn_to_redis()
mongo_coll = get_conn_to_mongo()



def distribution_of_alerts_by_limit_and_priority_level():
    redis_chsh = redis_client.get('queries')
    if redis_chsh:
        redis_chsh = str(redis_chsh)
        return {"source": "redis_cache", "value:": json.loads(redis_chsh)}
    else:
        query = {:}
        result_query = mongo_coll.aggregate(query)
        if result_query:
            try:
                redis_client.set("queries",json.dumps(result_query),3000)
                return {"source": "mongo","valu": result_query}
            except  Exception as e:
                print(e)
                return {"error":"{e}"}



def The_five_zones_with_the_highest_number_of_urgent_alerts():
    redis_chsh = redis_client.get('queries')
    if redis_chsh:
        redis_chsh = str(redis_chsh)
        return {"source": "redis_cache", "value:": json.loads(redis_chsh)}
    else:
        query = {:}
        result_query = mongo_coll.aggregate(query)
        if result_query:
            try:
                redis_client.set("queries",json.dumps(result_query),3000)
                return {"source": "mongo","valu": result_query}
            except  Exception as e:
                print(e)
                return {"error":"{e}"}
            

def how_are_the_alerts_distributed_according_to_distance_ranges_from_the_fence():
    redis_chsh = redis_client.get('queries')
    if redis_chsh:
        redis_chsh = str(redis_chsh)
        return {"source": "redis_cache", "value:": json.loads(redis_chsh)}
    else:
        query = {:}
        result_query = mongo_coll.aggregate(query)
        if result_query:
            try:
                redis_client.set("queries",json.dumps(result_query),3000)
                return {"source": "mongo","valu": result_query}
            except  Exception as e:
                print(e)
                return {"error":"{e}"}

def areas_characterized_by_a_high_number_of_alerts_here_a_significant_number_of_people_were_detected_in_low_visibility_conditions()
    redis_chsh = redis_client.get('queries')
    if redis_chsh:
        redis_chsh = str(redis_chsh)
        return {"source": "redis_cache", "value:": json.loads(redis_chsh)}
    else:
        query = {:}
        result_query = mongo_coll.aggregate(query)
        if result_query:
            try:
                redis_client.set("queries",json.dumps(result_query),3000)
                return {"source": "mongo","valu": result_query}
            except  Exception as e:
                print(e)
                return {"error":"{e}"}

def areas_that_constitute_risk_hotspots():
    redis_chsh = redis_client.get('queries')
    if redis_chsh:
        redis_chsh = str(redis_chsh)
        return {"source": "redis_cache", "value:": json.loads(redis_chsh)}
    else:
        query = {:}
        result_query = mongo_coll.aggregate(query)
        if result_query:
            try:
                redis_client.set("queries",json.dumps(result_query),3000)
                return {"source": "mongo","valu": result_query}
            except  Exception as e:
                print(e)
                return {"error":"{e}"}