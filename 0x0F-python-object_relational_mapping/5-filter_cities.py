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
        FROM cities
        WHERE cities.state_id = (SELECT states.id
        FROM states
        WHERE states.name = %s)
        ORDER BY cities.id ASC""", (user_input,)
    )

    query_result = cursor.fetchall()
    print(', '.join(["{:s}".format(result[0]) for result in query_result]))

    cursor.close()
    connection.close()
