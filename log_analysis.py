#! /usr/bin/env python3

import psycopg2


def connect(database_name="news"):
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print("<error message>")


def yourFunc():
    db, cursor = connect()

    query = ("select title, count (*) accesses from log join articles "
             "on substring(path, 10 , char_length(path)) = articles.slug "
             "group by articles.title order by count(*) desc fetch first "
             "3 rows only;")
    cursor.execute(query)
    print("Top 3 articles of all time:")
    print("")
    for (title, accesses) in cursor:
        print("{} - {} views".format(title, accesses))
    print("")
    query = ("select name, count (*) accesses from log join articles "
             "on substring(path, 10 , char_length(path)) = articles.slug "
             "join authors on articles.author = authors.id group by "
             "authors.name order by count(*) desc;")
    cursor.execute(query)
    print("Top authors of all time:")
    print("")
    for (name, accesses) in cursor:
        print("{} - {} views".format(name, accesses))
    print("")
    query = ("select to_char(date, 'FMMonth FMDD, YYYY') as date, "
             "err/total*100 as ratio from (select time::date as date, "
             "count(*) as total, sum((status != '200 OK')::int)::float as "
             "err from log group by date) as errors where err/total > 0.01;")
    cursor.execute(query)
    print("Days with more than 1% of requests errors:")
    print("")
    for (date, ratio) in cursor:
        print("{} - {} % errors".format(date, ratio))
    db.close()


yourFunc()
