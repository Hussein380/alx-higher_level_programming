#!/usr/bin/python3


"""
list all states with a name starting with N (upper N) from the
databse hbtn_0e_0_usa sorted in ascending order by states.id
"""
import MySQLdb
import sys
"""check whether the script is running directly  by the python interpreter
or if it is being imported as module"""
if __name__ == "__main__":
    """retrieve the argument passsed when executing the script"""
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    """establish connection to the MYSQL database"""
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
        print("Error connecting to database:{}".format(e))
        sys.exit(1)

    """creates a curso object"""
    cur = conn.cursor()

    """execute the SQL code using cursor execute() method"""
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N% '\
            ORDER BY states.id ASC")
    """fetch all rows"""
    rows = cur.fetchall()
    for row in rows:
        print(row)

    """close cursor and databse connection"""
    cur.close()
    cur.close()
