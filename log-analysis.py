#!/usr/bin/env python
import psycopg2


def most_popular_articles(cur):
    title = "Below are the list of most popular articles of all times."
    query = """select title, count(*) as num from articles,
            log where log.path like concat ('/article/', articles.slug)
            group by articles.title order by num desc limit 3;"""
    cur.execute(query)
    data = cur.fetchall()
    return data, title


def most_popular_author(cur):
    title = "Below are the list of most popular authors of all times."
    query = """select name, count(*) as num from articles, log,
            authors where log.path like concat ('/article/', articles.slug)
            and articles.author = authors.id group by authors.name
            order by num desc;"""
    cur.execute(query)
    data = cur.fetchall()
    return data, title


def percentage_error(cur):
    title = "Maximum percentage of error in a day."
    query = """select date_trunc('day',time)::date,
            round(100.0*sum(case log.status when '200 OK' then 0 else 1 end)
            /count(*),4) as ErrorPercentage from log group by
            date_trunc('day',time)::date order by ErrorPercentage
            desc limit 1;"""
    cur.execute(query)
    data = cur.fetchall()
    return data, title


def print_formatted_result(results, title):
    print ("\n")
    print (title)
    print ("------------------------")
    for result in results:
        print ("{} -- {}".format(result[0], result[1]))


if __name__ == "__main__":

    conn = psycopg2.connect("dbname=news user=vagrant")
    cur = conn.cursor()

    try:
        popular_articles, title = most_popular_articles(cur)
        print_formatted_result(popular_articles, title)
    except psycopg2.Error as e:
        print ("Failed to get the most popular articles of all times", e)

    try:
        popular_authors, title = most_popular_author(cur)
        print_formatted_result(popular_authors, title)
    except psycopg2.Error as e:
        print ("Failed to get the most popular author of all times", e)

    try:
        highest_error, title = percentage_error(cur)
        print_formatted_result(highest_error, title)
    except psycopg2.Error as e:
        print ("Maximum percentage of error in a day", e)

    cur.close()
    conn.close()
