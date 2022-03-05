#!/usr/bin/python3
"""
that takes in an argument and displays all values in the states table
 of hbtn_0e_0_usa where name matches the argument.
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    dbName = sys.argv[3]
    nameSearch = str(sys.argv[4])

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=dbName)

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name=('{}') ORDER BY id ASC"
                .format(nameSearch))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
