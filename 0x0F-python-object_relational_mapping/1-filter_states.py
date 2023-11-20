#!/usr/bin/python3
"""
script that lists all states  with a name starting with N
from the database hbtn_0e_0_usa
"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    username = argv[1]
    password = argv[2]
    dbName = argv[3]

    conn = MySQLdb.connect(
            host="localhost", port=3306, user=username,
            passwd=password, db=dbName, charset="utf8"
            )
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1][0] == 'N':
            print(row)
    cur.close()
    conn.close()
