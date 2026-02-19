from fastapi import FastAPI
from pymongo import MongoClient
import uvicorn
import os
import json
import redis
from dal import *


## fastapi
app = FastAPI()

@app.get("/analytics/alerts-by-border-and-priority")
def distribution_of_alerts_by_limit_and_priority_level1():
    result = distribution_of_alerts_by_limit_and_priority_level()
    return {"":result}
    
    

@app.get("/analytics/top-urgent-zones")
def The_five_zones_with_the_highest_number_of_urgent_alerts1():
    result = The_five_zones_with_the_highest_number_of_urgent_alerts()
    return {"":result}

@app.get("/analytics/distance-distribution")
def how_are_the_alerts_distributed_according_to_distance_ranges_from_the_fence1():
    result = how_are_the_alerts_distributed_according_to_distance_ranges_from_the_fence()
    return {"":result}


@app.get(" /analytics/low-visibility-high-activity")
def areas_characterized_by_a_high_number_of_alerts_here_a_significant_number_of_people_were_detected_in_low_visibility_conditions1():
    result = areas_characterized_by_a_high_number_of_alerts_here_a_significant_number_of_people_were_detected_in_low_visibility_conditions()
    return {"":result}


@app.get("/analytics/hot-zones")
def areas_that_constitute_risk_hotspots1():
    result = areas_that_constitute_risk_hotspots()
    return {"":result}


























