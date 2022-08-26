#!/usr/bin/python3

import psycopg2

conn = psycopg2.connect(host="127.0.0.1", database="suppliers", user="postgres", password="uppercut100")

if conn is not None:
    print("Connection established to PostgreSQL.")
else:
    print("Connection not established to PostgreSQL.")
