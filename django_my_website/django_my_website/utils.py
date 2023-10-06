from db import get_running_data, get_other_data
from django.http import HttpRequest
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from config import IMAGES_FOLDER_PATH, BOT_API_TOKEN, CHAT_ROOM_ID
import telebot


def generate_matplotlib_graph(x, y, xlabel, ylabel, title, filename):
    matplotlib.use("agg")
    plt.bar(x, y)
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=28))
    plt.xlabel(xlabel=xlabel)
    plt.ylabel(ylabel=ylabel)
    plt.title(title)
    plt.savefig(f"{IMAGES_FOLDER_PATH}/{filename}", format="webp")
    plt.clf()


def generate_graph():
    running_data = get_running_data(last_7_days=False)
    date_list = []
    running_list = []
    running_time_list = []
    for row in running_data:
        date_list.append(row["day"])
        running_time_list.append(row["duration"])
        running_list.append(row["distance"])

    pace_list = []
    for i in range(len(running_list)):
        try:
            pace_list.append(running_time_list[i] / running_list[i])
        except ZeroDivisionError:
            pace_list.append(0)

    generate_matplotlib_graph(x=date_list, y=running_list,
                              xlabel="Ngày chạy",
                              ylabel="Quãng đường chạy(km)",
                              title="Biểu đồ theo dõi quãng đường chạy",
                              filename="distance.webp")

    generate_matplotlib_graph(x=date_list, y=pace_list,
                              xlabel="Ngày chạy",
                              ylabel="Pace chạy(phút/km)",
                              title="Biểu đồ theo dõi pace chạy",
                              filename="pace.webp")

    generate_matplotlib_graph(x=date_list, y=running_time_list,
                              xlabel="Ngày chạy",
                              ylabel="Thời gian chạy",
                              title="Biểu đồ theo dõi thời gian chạy",
                              filename="duration.webp")

    running_data = get_running_data(last_7_days=True)
    date_list = []
    running_list = []
    running_time_list = []
    for row in running_data:
        date_list.append(row["day"])
        running_time_list.append(row["duration"])
        running_list.append(row["distance"])
    pace_list = []
    for i in range(len(running_list)):
        try:
            pace_list.append(running_time_list[i] / running_list[i])
        except ZeroDivisionError:
            pace_list.append(0)

    generate_matplotlib_graph(x=date_list, y=running_time_list,
                              xlabel="Ngày chạy",
                              ylabel="Quãng đường chạy(km)",
                              title="Biểu đồ theo dõi quãng đường chạy",
                              filename="distance-7-days.webp")

    generate_matplotlib_graph(x=date_list, y=pace_list,
                              xlabel="Ngày chạy",
                              ylabel="Pace chạy (phút/km)",
                              title="Biểu đồ theo dõi pace chạy",
                              filename="pace-7-days.webp",
                              )

    generate_matplotlib_graph(x=date_list, y=running_time_list,
                              xlabel="Ngày chạy",
                              ylabel="Thời gian chạy(phút)",
                              title="Biểu đồ theo dõi thời gian chạy",
                              filename="duration-7-days.webp")

    date_list = []
    study_time = []
    play_time = []
    for row in get_other_data():
        date_list.append(row["date"])
        study_time.append(row["study_time"])
        play_time.append(row["play_time"])

    generate_matplotlib_graph(x=date_list, y=study_time,
                              xlabel="Ngày",
                              ylabel="Thời gian học (phút)",
                              title="Biểu đồ theo dõi thời gian học",
                              filename="study.webp")

    generate_matplotlib_graph(x=date_list, y=play_time,
                              xlabel="Ngày",
                              ylabel="Thời gian chơi (phút)",
                              title="Biểu đồ theo dõi thời gian chơi",
                              filename="play.webp")


def send_telegram_notification(message: str):
    bot = telebot.TeleBot(BOT_API_TOKEN)
    bot.send_message(CHAT_ROOM_ID, message)


def add_metadata(request: HttpRequest):
    """Return user agent of request"""
    user_agent = request.META["HTTP_USER_AGENT"]
    for bot in ["http://www.google.com/bot.html", "http://www.bing.com/bingbot.htm"]:
        if bot in user_agent:
            return None
    message = "\n User-Agent: " + user_agent
    message += "\n Ip Address: " + request.META["REMOTE_ADRD"]
    return message


if __name__ == "__main__":
    generate_graph()
