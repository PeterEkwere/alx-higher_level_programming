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
    state_name = sys.argv[4]
    city_list = []
    cities = ""

    connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            password=password,
            database=dbname,
            charset="utf8"
            )

    cursor = connection.cursor()
    query = """
    SELECT `c`.`id`, `c`.`name`, `s`.`name` \
    FROM cities AS c \
    INNER JOIN states as `s` ON `c`.`state_id` = `s`.`id` \
    ORDER BY `c`.`id`
    """
    cursor.execute(query)
    query_rows = cursor.fetchall()
    for rows in query_rows:
        city_id, city_name, state_n = rows
        if state_n == state_name:
            city_list.append(city_name)
    cities = ", ".join(city_list)
    print(cities)
    cursor.close()
    connection.close()
