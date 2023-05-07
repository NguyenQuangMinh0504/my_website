from redis import Redis
running_table = Redis(host="127.0.0.1", port=6379, db=0)

user_table = [
    {"username": "nguyenquangminh", "password": "123", "cookie": "cookie1"},
    {"username": "nguyenminh2", "password": "1234", "cookie": "cookie2"},
]
