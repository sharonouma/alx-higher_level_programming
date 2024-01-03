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
    cur.execute("SELECT * FROM cities\
            JOIN states ON cities.state_id = states.id\
            WHERE states.name = %s\
            ORDER BY cities.id ASC", params)
    query_rows = cur.fetchall()
    lst = []
    for row in query_rows:
        if row[4] == params[0]:
            lst.append(row[2])
    print(', '.join(lst))
    cur.close()
    conn.close()
