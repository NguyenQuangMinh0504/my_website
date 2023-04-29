import redis
import json
from datetime import datetime, timedelta
redis_client = redis.Redis(host="127.0.0.1", port=6379, db=0)
start_date = datetime(year=2023, month=4, day=10)
running_list = [2, 3.02, 4.02, 3.55, 3.03, 4.76, 3.02, 2.77, 2.67,
                3.17, 3.45, 3.42, 4.54, 5.3,
                2.86, 3.68, 3.76, 3.84, 3.83, 5.62]
running_time_list = [30, 30, 30, 30, 30, 45, 30, 30,
                     30, 30, 30, 30, 45, 45,
                     30, 30, 30, 30, 30, 45]
i = 0
while start_date.date() <= datetime.today().date():
    redis_client.set(start_date.strftime("%x"), json.dumps({"time": running_time_list[i], "distance": running_list[i]}))
    i += 1
    start_date = start_date + timedelta(days=1)