from mysql import connector
from config import DB_HOST, DB_PASSWORD


def execute(database: str, query: str, fetch: str, args: tuple = None):
    cnx = connector.connect(user="root",
                            password=DB_PASSWORD,
                            database=database,
                            host=DB_HOST)
    cnx.autocommit = True
    cursor = cnx.cursor(dictionary=True)

    if args is not None:
        cursor.execute(query, args)
    else:
        cursor.execute(query)

    result = None
    if fetch == "all":
        result = cursor.fetchall()
    elif fetch == "one":
        result = cursor.fetchone()
    cursor.close()
    cnx.close()
    return result


def get_running_data(last_7_days=False):
    if last_7_days is True:
        return execute(
            database="my_data",
            query="SELECT * FROM running_data ORDER BY day DESC LIMIT 7",
            fetch="all")
    return execute(database="my_data",
                   query="SELECT * FROM running_data ORDER BY day",
                   fetch="all")


def add_running_data(date: str, duration: int, distance: float):
    return execute(database="my_data",
                   query=f"""INSERT INTO running_data
                    VALUES('{date}', {duration}, {distance})""",
                   fetch=None
                   )


def add_other_data(date: str, study_time: int, play_time: int):
    return execute(database="my_data",
                   query=f"""INSERT INTO daily_activities
                    VALUES('{date}', {study_time}, {play_time})""",
                   fetch=None
                   )


def get_other_data():
    return execute(database="my_data",
                   query="SELECT * FROM daily_activities",
                   fetch="all")


def increment_view_counter(title: str):
    return execute(database="blog",
                   query=f"""UPDATE blog SET total_view = total_view + 1
                   WHERE title = '{title}'""", fetch=None)
