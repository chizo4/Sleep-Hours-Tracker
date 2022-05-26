'''
SLEEP HOURS TRACKER: Data handling and DB setup

Date created: 05/2022

Author: Filip J. Cierkosz
'''

import sqlite3
import pandas as pd
import datetime
import re

def init_db():
    '''
    Initialize the DB to store: record's ID, hours slept, current date (DD-MM-YYYY).
    '''
    db = sqlite3.connect('slept_hours.db')
    cursor = db.cursor()

    # Create a table with schema.
    cursor.execute('DROP TABLE IF EXISTS sleep_table')
    cursor.execute('''
                CREATE TABLE sleep_table (
                    id INTEGER PRIMARY KEY,
                    hours FLOAT,
                    date STRING
                )
            ''')

    # Commit the operations and close the DB.
    db.commit()
    db.close()
    print('The DB has been successfully initialized.')

def update_db(hr, dt):
    '''
    Update the database with new record (if correct and not exists).
    '''
    db = sqlite3.connect('slept_hours.db')
    cursor = db.cursor()

    # Check if the record for the date already exists in the table.
    cursor.execute('''SELECT date FROM sleep_table
                        WHERE date=?''', (dt))
    exist = cursor.fetchone()

    # correct float

    # correct date format

    if (not exist):
        try:
           return null
        except sqlite3.Error as e:
            print(f'Failed to update the DB. An error occurred:\n', e)
    else:
        print(f'The record for the date - {dt} - already exists in the DB.')


def print_records_db():
    '''
    Display the database records.
    '''
    try:
        # Connect with the DB, create dataframe and display all its contents.
        db = sqlite3.connect('slept_hours.db')
        df = pd.read_sql_query("SELECT * FROM sleep_table", db)
        print(df.to_string())
    except sqlite3.Error as e:
        print(f'Failed to process the DB record. An error occurred:\n', e)






# Initialize the database (executed only once, or when to reset the DB).
#init_db()

# Display all the database records.
print_records_db()



# test
#randomDate = datetime.datetime.today().strftime('%d/%m/%Y')
#print(type(randomDate))
