#!/usr/bin/python3
"""
Lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""
from sys import argv
import MySQLdb


if __name__ == "__main__":
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8",
    )
    cursor = connection.cursor()

    cursor.execute(
        """SELECT * FROM states
        WHERE name LIKE BINARY 'N%'
        ORDER BY id ASC"""
    )

    query_result = cursor.fetchall()
    for result in query_result:
        print(result)

    cursor.close()
    connection.close()
