#!/usr/bin/python3
"""
Takes in an argument and displays all values
in the states table of hbtn_0e_0_usa
where name matches the argument.
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
        """SELECT * FROM states
        WHERE name LIKE BINARY '{:s}'
        ORDER BY id ASC""".format(user_input)
    )

    query_result = cursor.fetchall()
    for result in query_result:
        print(result)

    cursor.close()
    connection.close()
