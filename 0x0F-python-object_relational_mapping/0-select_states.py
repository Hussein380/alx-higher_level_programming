#!/usr/bin/python3

"""
lists all the states from  the database hbtn_0e_0_usa sorted in ascending
order by states.id

"""

import MySQLdb

import sys

if __name__ == "__main__":
    """Retrieve MySQL username, password and database name from the cmd arguments """
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    """Attempting to establish a connection to the MYSQL datatbase """
    try:
        conn = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=mysql_username,
                passwd=mysql_password,
                db=db_name,
                charset="utf8"
                )
    except MySQLdb.Error as e:
        print("Error connecting to database: {}".format(e))
        sys.exit(1)

    """create a cursor object to execute SQL queries"""
    cur = conn.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC")

    """retrieve all rows returned by the sql query"""
    rows = cur.fetchall()

    for row in rows:
        print(row)

    """close the cursor and the daatabase connection to free up system resources """
    cur.close()
    conn.close()
