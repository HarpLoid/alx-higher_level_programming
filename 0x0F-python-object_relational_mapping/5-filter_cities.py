#!/usr/bin/python3
"""
Takes in the name of a state as an argument
and lists all cities of that state,
using the database hbtn_0e_4_usa
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

    user_input = argv[4]

    cursor.execute(
        """SELECT cities.name
        FROM states
        INNER JOIN cities ON states.id = cities.state_id
        WHERE states.name LIKE %s
        ORDER BY cities.id ASC""", (user_input,)
    )

    query_result = cursor.fetchall()
    for result in query_result:
        print("%s" % result, end="")
        print(", ", end="")
    print("\n")

    cursor.close()
    connection.close()
