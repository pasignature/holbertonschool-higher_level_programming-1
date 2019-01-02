#!/usr/bin/python3
'''
A script that lists all states with a name start with an N from
the database hbtn_0e_0_usa
'''

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
    db.close()
    rows = cur.fetchall()
    for row in rows:
        print("{}".format(row))
