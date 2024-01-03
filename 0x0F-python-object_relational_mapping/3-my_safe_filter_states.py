#!/usr/bin/python3
"""
script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument
"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    username = argv[1]
    password = argv[2]
    dbName = argv[3]
    params = (argv[4], )

    conn = MySQLdb.connect(
            host="localhost", port=3306, user=username,
            passwd=password, db=dbName, charset="utf8"
            )
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s\
            ORDER BY id ASC", params)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
