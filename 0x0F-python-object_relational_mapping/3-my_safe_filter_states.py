#!/usr/bin/python3

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
        WHERE name LIKE %s
        ORDER BY id ASC""", (user_input,)
    )

    query_result = cursor.fetchall()
    for result in query_result:
        print(result)

    cursor.close()
    connection.close()
