import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from db import cursor
from settings import PROJECT_PATH


def generate_graph():

    # Lấy data từ mysql database
    cursor.execute("SELECT * FROM running_data")
    running_data = cursor.fetchall()
    date_list = []
    running_list = []
    running_time_list = []
    for row in running_data:
        date_list.append(row[0])
        running_time_list.append(row[1])
        running_list.append(row[2])

    plt.clf()
    plt.xlabel("Ngày chạy")
    plt.ylabel("Quãng đường chạy(km)")
    plt.title("Biểu đồ theo dõi quãng đường chạy")
    plt.plot(date_list, running_list)
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=14))
    plt.savefig(f"{PROJECT_PATH}/running/static/running/images/distance.png")
    plt.clf()

    pace_list = []
    for i in range(len(running_list)):
        pace_list.append(running_time_list[i] / running_list[i])

    plt.xlabel("Ngày chạy")
    plt.ylabel("Pace chạy(phút/km)")
    plt.title("Biểu đồ theo dõi pace chạy")

    plt.plot(date_list, pace_list)
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=14))
    plt.axhline(y=8, color="red", linestyle="dashed")
    plt.savefig(f"{PROJECT_PATH}/running/static/running/images/pace.png")
    plt.clf()

    plt.xlabel("Ngày chạy")
    plt.ylabel("Thời gian chạy(phút)")
    plt.title("Biểu đồ theo dõi thời gian chạy")
    plt.bar(date_list, running_time_list)
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=14))
    plt.savefig(f"{PROJECT_PATH}/running/static/running/images/duration.png")
    plt.clf()


if __name__ == "__main__":
    generate_graph()
