import sqlite3
from eli import cur, con

#DEFINING A DATABASE TABLE
cur.execute(""" CREATE TABLE todos(
            id integer,
            todo text,
            status text
            )""")

