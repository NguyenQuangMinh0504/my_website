from mysql import connector
cnx = connector.connect(user="root", password="qmqmqm8c3", database="my_data")
cursor = cnx.cursor()


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
