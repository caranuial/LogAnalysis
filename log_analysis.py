import psycopg2

DBNAME = "news"


class DbQuerer():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select title, count (*) accesses " +
              "from log join articles on " +
              "substring(path, 10 , char_length(path)) = articles.slug " +
              "group by articles.title " +
              "order by count(*) desc " +
              "fetch first 3 rows only;")
    print("Top 3 articles of all time:")
    print("")
    for (title, accesses) in c:
        print("{} - {} views".format(title, accesses))
    print("")
    c.execute("select name, count (*) accesses " +
              "from log join articles on " +
              "substring(path, 10 , char_length(path)) = articles.slug " +
              "join authors on articles.author = authors.id " +
              "group by authors.name " +
              "order by count(*) desc;")
    print("Days with more than 1% of requests errors:")
    print("")
    for (name, accesses) in c:
        print("{} - {} views".format(name, accesses))
    print("")
    c.execute("select a.date as date, " +
              "round((bad_requests::decimal / requests) * 100,3) " +
              "as perc_of_bad_req, bad_requests, requests from " +
              "(select to_char(time, 'dd/mm/yyyy') as date, count(*) " +
              "bad_requests from log where status <> '200 OK' " +
              "group by to_char(time, 'dd/mm/yyyy')) as a join " +
              "(select to_char(time, 'dd/mm/yyyy') as date, count(*) " +
              "requests from log where path <> '/' group by " +
              "to_char(time, 'dd/mm/yyyy')) as b on a.date = b.date where " +
              "(bad_requests::decimal / requests) * 100 >= 1;")
    print("Top authors of all time:")
    print("")
    for (date, perc_of_bad_req, bad_requests, requests) in c:
        print("{} - {} % errors - bad {} all {}".format(date,
                                                        perc_of_bad_req,
                                                        bad_requests,
                                                        requests))
    db.close()
