# lib/config.py
import sqlite3

CONN = sqlite3.connect('company.db')  # is a constant equal to a hash that contains a connection to the database.
CURSOR = CONN.cursor()   #is a constant that allows us to interact with the database and execute SQL statements
