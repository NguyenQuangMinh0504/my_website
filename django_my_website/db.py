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


def get_blog_detail(title):
    return execute(database="blog",
                   query="SELECT * FROM blog WHERE title = %s",
                   fetch="one",
                   args=(title,))


def get_all_blog(order: str = None):
    if order == "views":
        return execute(database="blog",
                       query="SELECT * FROM blog ORDER BY total_view DESC",
                       fetch="all")
    return execute(database="blog",
                   query="SELECT * FROM blog ORDER BY id DESC",
                   fetch="all")


def get_all_comment(blog_id):
    return execute(database="blog",
                   query="SELECT * FROM comment WHERE blog_id = %s",
                   fetch="all",
                   args=(blog_id,))


def add_comment(blog_id, content):
    return execute(
        database="blog",
        query="INSERT INTO comment (content, blog_id) VALUES(%s, %s)",
        fetch=None,
        args=(content, blog_id)
        )


def get_running_data(last_7_days=False):
    if last_7_days is True:
        return execute(
            database="my_data",
            query="SELECT * FROM running_data ORDER BY day DESC LIMIT 7",
            fetch="all")
    return execute(database="my_data",
                   query="SELECT * FROM running_data ORDER BY day",
                   fetch="all")


def edit_blog(old_title, new_title, snippet, content):
    return execute(
        database="blog",
        query="""UPDATE blog SET title = %s,
                 snippet = %s, content = %s WHERE title = %s""",
        fetch=None,
        args=(new_title, snippet, content, old_title))


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


def get_all_tag():
    return execute(database="blog",
                   query="SELECT name FROM tag",
                   fetch="all")


def get_blog_tag(blog_id: int):
    return execute(
        database="blog",
        query="SELECT name FROM blog_tag INNER JOIN tag ON blog_tag.tag_id = tag.id WHERE blog_id = %s",
        fetch="all",
        args=(blog_id, ),
        )


def get_all_blog_with_tag(tag_name):
    return execute(
        database="blog",
        query="SELECT blog.* FROM blog INNER JOIN blog_tag ON blog.id = blog_tag.blog_id INNER JOIN tag ON blog_tag.tag_id = tag.id WHERE tag.name = %s",
        fetch="all",
        args=(tag_name, ),
    )
