import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta
import json
from db import running_table
from settings import PROJECT_PATH


def generate_graph():
    
    start_date = datetime(year=2023, month=4, day=10)
    end_date = datetime.now()
    date_list = []
    running_list = []
    running_time_list = []

    while start_date < end_date:
        running_data = running_table.get(start_date.strftime("%x"))
        if running_data is not None:
            running_data = json.loads(running_data.decode("utf-8"))
            running_list.append(running_data["distance"])
            running_time_list.append(running_data["time"])
            date_list.append(start_date.strftime("%x"))
        start_date += timedelta(days=1)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=7))
    plt.plot(date_list, running_list)
    plt.savefig(f"{PROJECT_PATH}/running/static/running/images/distance.png")
    plt.clf()
    pace_list = []
    for i in range(len(running_list)):
        pace_list.append(running_time_list[i] / running_list[i])
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=7))
    plt.plot(date_list, pace_list)
    plt.axhline(y=8, color="red", linestyle="dashed")
    plt.savefig(f"{PROJECT_PATH}/running/static/running/images/pace.png")
    plt.clf()
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=7))
    plt.bar(date_list, running_time_list)
    plt.savefig(f"{PROJECT_PATH}/running/static/running/images/duration.png")


if __name__ == "__main__":
    generate_graph()
