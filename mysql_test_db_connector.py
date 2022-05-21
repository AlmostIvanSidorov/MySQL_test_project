"""
Some MySQL connector tests
"""

import mysql.connector
from mysql.connector import Error
from configs.config import db_config


def create_mysql_db_connection(db_host,user_name, user_password, db_name=None):
    connection_db = None
    try:
        connection_db = mysql.connector.connect(
            host=db_host,
            user=user_name,
            password=user_password,
            database=db_name
        )
        print("MySQL connected")
    except Error as db_connection_error:
        print("Error appeared:", db_connection_error)
    return connection_db

def create_mysql_db(db_name='first_test2'):
    db_name = db_name
    conn = create_mysql_db_connection(db_config["mysql"]["host"],
                                      db_config["mysql"]["user"],
                                      db_config["mysql"]["pass"]
                                      )

    cursor = conn.cursor()

    cursor.execute(f"CREATE DATABASE {db_name}")

    cursor.close()
    conn.close()


def connect_mysql_db(db_name='first_test2'):
    db_name = db_name

    conn = create_mysql_db_connection(db_config["mysql"]["host"],
                                      db_config["mysql"]["user"],
                                      db_config["mysql"]["pass"],
                                      db_name
                                      )
    try:
        cursor = conn.cursor()
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT,
        name TEXT NOT NULL,
        age INT,
        PRIMARY KEY (id)
        ) ENGINE = InnoDB'''

        cursor.execute(create_table_query)
        conn.commit()

    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()


def main():
    connect_mysql_db()


if __name__ == "__main__":
    main()
