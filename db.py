from redis import Redis
from mysql import connector
cnx = connector.connect(user="root", password="qmqmqm8c3", database="my_data")
cursor = cnx.cursor()
running_table = Redis(host="127.0.0.1", port=6379, db=0)
