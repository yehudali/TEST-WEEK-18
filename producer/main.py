from edis_connection import get_conn_to_redis
from priority_logic import read_csv_file, priority_classification_rules, check_if_urgent_and_insert_to_redis
from typing import Any
import json
def run():
    redis_client = get_conn_to_redis()
    data1 = read_csv_file()
    data2 = priority_classification_rules(data1)

    check_if_urgent_and_insert_to_redis(redis_client, data=data2)


if __name__ == "__main__":
    run()