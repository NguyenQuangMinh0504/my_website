from mysql import connector


def get_blog_detail(title):
    cnx = connector.connect(user="root",
                            password="qmqmqm8c3",
                            database="blog"
                            )
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(
        f"SELECT * FROM blog WHERE title = '{title}'"
        )
    result = cursor.fetchone()
    cursor.close()
    cnx.close()
    return result


def add_blog(title, snippet, content):
    cnx = connector.connect(user="root",
                            password="qmqmqm8c3",
                            database="blog"
                            )
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(
        f"""
        INSERT INTO blog (title, snippet, content)
         VALUES ('{title}', '{snippet}', '{content}')
        """
        )
    cnx.commit()
    cursor.close()
    cnx.close()


def get_all_blog():
    cnx = connector.connect(user="root",
                            password="qmqmqm8c3",
                            database="blog"
                            )
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(
        "SELECT * FROM blog"
    )
    result = cursor.fetchall()
    cursor.close()
    cnx.close()
    return result


def get_all_comment(blog_id):
    cnx = connector.connect(user="root",
                            password="qmqmqm8c3",
                            database="blog"
                            )
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM comment WHERE blog_id = {blog_id}")
    result = cursor.fetchall()
    cursor.close()
    cnx.close()
    return result


def add_comment(blog_id, content):
    cnx = connector.connect(user="root",
                            password="qmqmqm8c3",
                            database="blog"
                            )
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(
        f"""INSERT INTO comment (content, blog_id)
         VALUES('{content}', {blog_id})""")
    cnx.commit()
    cursor.close()
    cnx.close()


def get_running_data():
    cnx = connector.connect(user="root",
                            password="qmqmqm8c3",
                            database="my_data")
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM running_data")
    result = cursor.fetchall()
    cursor.close()
    cnx.close()
    return result


def edit_blog(old_title, new_title, snippet, content):
    cnx = connector.connect(user="root",
                            password="qmqmqm8c3",
                            database="blog"
                            )
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(
        f"""
        UPDATE blog SET title = '{new_title}', snippet = '{snippet}',
         content = '{content}' WHERE title = '{old_title}';
        """
        )
    cnx.commit()
    cursor.close()
    cnx.close()


def increment_view_counter(title: str):
    cnx = connector.connect(user="root",
                            password="qmqmqm8c3",
                            database="blog")
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(f"UPDATE blog SET total_view = total_view + 1 WHERE title = '{title}'")
    cnx.commit()
    cursor.close()
    cnx.close()
