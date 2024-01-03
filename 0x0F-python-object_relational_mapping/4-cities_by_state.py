#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
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
    cur.execute("SELECT cities.id,cities.name,states.name FROM cities\
            JOIN states ON cities.state_id = states.id ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
