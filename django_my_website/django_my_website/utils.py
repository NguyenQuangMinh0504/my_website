"""Util function"""
from django.http import HttpRequest
import telebot
from ip2geotools.databases.noncommercial import DbIpCity
from config import BOT_API_TOKEN, CHAT_ROOM_ID


def send_telegram_notification(message: str):
    """Sending notification to telegram chat room"""
    bot = telebot.TeleBot(BOT_API_TOKEN)
    bot.send_message(CHAT_ROOM_ID, message)


def get_ip_location(ip_address: str):
    """Return location of request from ip"""
    try:
        response = DbIpCity.get(ip_address, api_key='free')  # 'free' key for the free non-commercial version
        city = response.city
        region = response.region
        country = response.country
        location = f"{city}, {region}, {country}"
        return location
    except Exception as e:
        print(f"Error: {e}")
        return None


def add_metadata(request: HttpRequest) -> str:
    """Return meta data of request"""
    user_agent = request.META["HTTP_USER_AGENT"]
    for bot in ["http://www.google.com/bot.html",
                "http://www.bing.com/bingbot.htm",
                "spider-feedback@bytedance.com",
                "IonCrawl"]:
        if bot in user_agent:
            return ""
    message = "\n User-Agent: " + user_agent
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    ip = None
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    message += "\n Ip Address: " + ip
    message += "\n Location: " + get_ip_location(ip_address=ip)
    return message
