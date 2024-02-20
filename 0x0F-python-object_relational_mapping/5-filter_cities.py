#!/usr/bin/python3
"""  takes in the name of a state as an
argument and lists all cities of that state,
using the database hbtn_0e_4_usa  """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    q = """ SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s"""
    cur.execute(q, (sys.argv[4],))
    rows = cur.fetchall()
    """
    tmp = list(row[0] for row in rows):
    This is a list comprehension that
    iterates over each row in rows and
    extracts the first element (row[0]) from
    each row, creating a list of these first elements.
    """
    tmp = list(row[0] for row in rows)
    """ The *tmp syntax unpacks the list into
    separate arguments for the print() function."""
    print(*tmp, sep=", ")
    cur.close()
    db.close()
