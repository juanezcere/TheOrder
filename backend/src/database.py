import pymysql.cursors
from flask import g


def connect():
    """
    Function to connect to database.
    """
    return pymysql.connect(
        host=g.config['database']['host'],
        user=g.config['database']['username'],
        password=g.config['database']['password'],
        db=g.config['database']['database'],
        cursorclass=pymysql.cursors.DictCursor
    )


def write(sql, registers):
    """
    Function to write data to database.
    """
    connection = connect()
    with connection:
        with connection.cursor() as cursor:
            for register in registers:
                cursor.execute(sql, register)
        connection.commit()


def read(sql, registers=[]):
    """
    Function to read data from database.
    """
    result = None
    connection = connect()
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(sql, registers)
            result = cursor.fetchall()
    return result
