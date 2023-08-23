from db import get_running_data
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from config import IMAGES_FOLDER_PATH


def generate_graph():

    running_data = get_running_data(last_7_days=False)
    date_list = []
    running_list = []
    running_time_list = []
    for row in running_data:
        date_list.append(row["day"])
        running_time_list.append(row["duration"])
        running_list.append(row["distance"])

    plt.clf()
    plt.xlabel("Ngày chạy")
    plt.ylabel("Quãng đường chạy(km)")
    plt.title("Biểu đồ theo dõi quãng đường chạy")
    plt.bar(date_list, running_list)
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=28))
    plt.savefig(f"{IMAGES_FOLDER_PATH}/distance.webp", format="webp")
    plt.clf()

    pace_list = []
    for i in range(len(running_list)):
        try:
            pace_list.append(running_time_list[i] / running_list[i])
        except ZeroDivisionError:
            pace_list.append(0)

    plt.xlabel("Ngày chạy")
    plt.ylabel("Pace chạy(phút/km)")
    plt.title("Biểu đồ theo dõi pace chạy")

    plt.bar(date_list, pace_list)
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=28))
    plt.axhline(y=8, color="red", linestyle="dashed")
    plt.savefig(f"{IMAGES_FOLDER_PATH}/pace.webp", format="webp")
    plt.clf()

    plt.xlabel("Ngày chạy")
    plt.ylabel("Thời gian chạy(phút)")
    plt.title("Biểu đồ theo dõi thời gian chạy")
    plt.bar(date_list, running_time_list)
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=28))
    plt.savefig(f"{IMAGES_FOLDER_PATH}/duration.webp", format="webp")
    plt.clf()

    running_data = get_running_data(last_7_days=True)
    date_list = []
    running_list = []
    running_time_list = []
    for row in running_data:
        date_list.append(row["day"])
        running_time_list.append(row["duration"])
        running_list.append(row["distance"])

    plt.clf()
    plt.xlabel("Ngày chạy")
    plt.ylabel("Quãng đường chạy(km)")
    plt.title("Biểu đồ theo dõi quãng đường chạy")
    plt.bar(date_list, running_list)
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=28))
    plt.savefig(f"{IMAGES_FOLDER_PATH}/distance-7-days.webp", format="webp")
    plt.clf()

    pace_list = []
    for i in range(len(running_list)):
        try:
            pace_list.append(running_time_list[i] / running_list[i])
        except ZeroDivisionError:
            pace_list.append(0)

    plt.xlabel("Ngày chạy")
    plt.ylabel("Pace chạy(phút/km)")
    plt.title("Biểu đồ theo dõi pace chạy")

    plt.bar(date_list, pace_list)
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=28))
    plt.axhline(y=8, color="red", linestyle="dashed")
    plt.savefig(f"{IMAGES_FOLDER_PATH}/pace-7-days.webp", format="webp")
    plt.clf()

    plt.xlabel("Ngày chạy")
    plt.ylabel("Thời gian chạy(phút)")
    plt.title("Biểu đồ theo dõi thời gian chạy")
    plt.bar(date_list, running_time_list)
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=28))
    plt.savefig(f"{IMAGES_FOLDER_PATH}/duration-7-days.webp", format="webp")
    plt.clf()


if __name__ == "__main__":
    generate_graph()
