#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa
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
        """SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states
        WHERE cities.state_id = states.id
        ORDER BY cities.id ASC"""
    )

    query_result = cursor.fetchall()
    for result in query_result:
        print(result)

    cursor.close()
    connection.close()
