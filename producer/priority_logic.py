from typing import Any
import json



def read_csv_file(): 
    path =r"border_alerts.json"
    with open("border_alerts.json",'r') as file:
        data = json.load(file)
        
        return data
    
        # for i in data:
            # print(i)
            ## {'border': 'lebanon', 'zone': 'zone-8', 'timestamp': '2026-02-13T00:32:01.281709', 'people_count': 1, 'weapons_count': 0, 'vehicle_type': 'car', 'distance_from_fence_m': 396, 'visibility_quality': 0.43}
            ## {'border': 'jordan', 'zone': 'zone-6', 'timestamp': '2026-02-16T18:06:10.363960', 'people_count': 20, 'weapons_count': 0, 'vehicle_type': 'car', 'distance_from_fence_m': 477, 'visibility_quality': 0.88}
        


def priority_classification_rules(data:dict):
    for repo in data:
        if repo['weapons_count']>0 or repo['distance_from_fence_m']<=50 or repo['people_count'] >= 8  or repo['vehicle_type'] == "truck": 
            repo["priority"] = "URGENT"

        elif (repo['distance_from_fence_m'] <= 50 and repo['people_count']) or (repo['vehicle_type'] == "jeep" and repo['people_count'] >= 3):
            repo["priority"] = "URGENT"
        
        else:
            repo["priority"] = "NORMAL"
    return data

def check_if_urgent_and_insert_to_redis(redis_client, data):
    for repo in data:
        if repo["priority"] == "URGENT":
            r = json.dumps(repo).encode("utf-8")
            redis_client.lpush(name="queue_urgent",value=r)

        elif repo["priority"] == "NORMAL":
            r = json.dumps(repo).encode("utf-8")
            redis_client.lpush(name="queue_normal",value=r)
            
        else:
            r = json.dumps(repo).encode("utf-8")
            redis_client.lpush(name="queue_normal",value=r)



