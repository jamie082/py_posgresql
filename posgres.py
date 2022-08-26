#!/usr/bin/python3

import psycopg2

conn = psycopg2.connect(host="localhost", database="postgres", user="postgres")

if conn is not None:
    print("Connection established to PostgreSQL.")
else:
    print("Connection not established to PostgreSQL.")
