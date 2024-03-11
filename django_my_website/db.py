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


def increment_view_counter(title: str):
    return execute(database="blog",
                   query=f"""UPDATE blog SET total_view = total_view + 1
                   WHERE title = '{title}'""", fetch=None)
