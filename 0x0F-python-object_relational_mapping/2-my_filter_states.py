#!/usr/bin/python3
# -*- encoding: UTF-8 -*-
"""
    This Script would query the Database and print all states
    Author: Peter Ekwere
"""
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    sort_by = sys.argv[4]

    connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            password=password,
            database=dbname,
            charset="utf8"
            )

    cursor = connection.cursor()
    query = "SELECT * FROM states WHERE name = %s"
    cursor.execute(query, (sort_by,))
    query_rows = cursor.fetchall()
    for rows in query_rows:
        if rows[1] == sort_by:
            print(rows)
    cursor.close()
    connection.close()
