import sqlite3

def create_user_table(cursor):

  cursor.execute(""" CREATE TABLE IF NOT EXISTS discord_users (

      user_id INTEGER NOT NULL PRIMARY KEY,
      study_list TEXT

  )""")

def load_database():

    connection = sqlite3.connect("./cogs/database/discord_users.db")
    cursor = connection.cursor()
    create_user_table(cursor)

    print("Database loaded successfully")