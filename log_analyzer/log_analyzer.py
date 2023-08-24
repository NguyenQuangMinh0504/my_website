from prometheus_client import start_http_server, Counter
import re
import time
import os
import dotenv
dotenv.load_dotenv("../django_my_website/.env")
ACCESS_LOG_PATH = os.getenv("ACCESS_LOG_PATH")
log_format = r'(?P<remote_addr>\S+) \[(?P<time_iso8601>.*?)\] ' \
    r'(?P<http_host>.*) "(?P<request>.*)" (?P<status>\d+)' \
    r'(?P<body_bytes_sent>\d+) (?P<http_referer>.*) "(?P<http_user_agent>.*)"'

access_counter = Counter(name="access",
                         documentation="IP access",
                         labelnames=["client_ip"])

start_http_server(port=8193)

with open(file=ACCESS_LOG_PATH, mode="r") as f:
    initial_position = f.tell()
while True:
    with open(ACCESS_LOG_PATH, "r") as f:
        f.seek(initial_position)
        for i in f:
            match = re.match(log_format, i)
            if match:
                client_ip = match.group("remote_addr")
                # Increment prometheus counter
                access_counter.labels(client_ip=client_ip).inc(amount=1)
        initial_position = f.tell()
        time.sleep(5)
