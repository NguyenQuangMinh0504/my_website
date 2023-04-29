import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from redis import Redis
import json
redis_client = Redis(host="127.0.0.1", port=6379, db=0)

start_date = datetime(year=2023, month=4, day=10)
end_date = datetime.now()
date_list = []
running_list = []
running_time_list = []

while start_date.day <= end_date.day:
    date_list.append(start_date.strftime("%d"))
    running_data = json.loads(
        redis_client.get(start_date.strftime("%x")).decode("utf-8")
        )
    running_list.append(running_data["distance"])
    running_time_list.append(running_data["time"])
    start_date += timedelta(days=1)
plt.plot(date_list, running_list)
plt.savefig("../running/static/running/images/distance.png")
plt.clf()
pace_list = []
for i in range(len(running_list)):
    pace_list.append(running_time_list[i] / running_list[i])
plt.plot(date_list, pace_list)
plt.axhline(y=8, color="red", linestyle="dashed")
plt.savefig("../running/static/running/images/pace.png")
plt.clf()
plt.bar(date_list, running_time_list)
plt.savefig("../running/static/running/images/duration.png")
