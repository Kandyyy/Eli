import sqlite3
from eli import cur, con

#DEFINING A DATABASE TABLE
def CreateTable():
    cur.execute(""" CREATE TABLE IF NOT EXISTS todos(
                id integer,
                todo text,
                status text
                )""")

CreateTable()