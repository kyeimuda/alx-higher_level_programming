#!/usr/bin/python3
""" a script that lists all cities from the database hbtn_0e_4_usa """

if __name__ == "__main__":
    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    dbName = sys.argv[3]
    stateSearch = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=dbName)
    cur = db.cursor()
    cur.execute("SELECT cities.name\
     FROM cities\
     JOIN states ON cities.state_id = states.id\
     WHERE states.name = ('{}')\
     ORDER BY cities.id ASC".format(stateSearch))

    rows = [r[0] for r in cur.fetchall()]
    if rows == []:
        print()
        
    for row in rows:
        listLength = len(rows)
        if row == rows[0]:
            list = row
            print(list, end="")
        elif row == rows[listLength - 1]:
            list = row
            print(", " + list)
        else:
            list = row
            print(", " + list, end="")

    cur.close()
    db.close()
