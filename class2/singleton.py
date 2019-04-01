i#!/usr/bin/env python3

class DBConnection:
    pass


if __name__ == '__main__':
    conn = DBConnection.get_instance()  # print "connect to db"
    conn.query()  # print "Make a query"

    conn = DBConnection.get_instance()  # print nothing
    conn.query()  # print "Make a query"
