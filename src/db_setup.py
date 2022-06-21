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

    # Table and schema.
    cursor.execute('DROP TABLE IF EXISTS sleep_table')
    cursor.execute('''
                CREATE TABLE sleep_table (
                    id INTEGER PRIMARY KEY,
                    hours FLOAT,
                    date STRING
                )
            ''')

    # Commit operations and close DB.
    db.commit()
    db.close()
    print('The DB has been successfully initialized.')

def check_date_exists(dt):
    '''
    Check if the record for the date already exists in the table.
    '''
    db = sqlite3.connect('slept_hours.db')
    cursor = db.cursor()
    cursor.execute('''SELECT date FROM sleep_table
                        WHERE date=?''', (dt,))
    return cursor.fetchone()

def validate_hours(hr):
    '''
    Validate hours, i.e. check if it is float and has correct format.
    '''
    regex_hours = '[+]?[0-9]+\.[0-9]+'
    correct_hours = re.search(regex_hours, str(hr))

    if (type(hr)==float and correct_hours):
        return True

    return False

def validate_date(dt):
    '''
    Validate date, i.e. check if it has format DD/MM/YYYY.
    '''
    regex_date = '^(((0[1-9]|[12][0-9]|30)[/]?(0[13-9]|1[012])|31[/]?(0[13578]|1[02])|(0[1-9]|1[0-9]|2[0-8])[/]?02)[/]?[0-9]{4}|29[/]?02[/]?([0-9]{2}(([2468][048]|[02468][48])|[13579][26])|([13579][26]|[02468][048]|0[0-9]|1[0-6])00))$'
    
    if (re.search(regex_date, dt)):
        return True

    return False

def update_db(hr, dt):
    '''
    Update the database with new record (if correct and not exists).
    '''
    # check if date already exists
    date_exists = check_date_exists(dt)

    # correct float
    correct_hours = validate_hours(hr)
    
    # correct date format
    correct_date = validate_date(dt)

    if ((not date_exists) and correct_hours and correct_date):
        try:
            db = sqlite3.connect('slept_hours.db')
            cursor = db.cursor()

            # Insert data into the DB.
            data = (hr, dt)
            insert_data_command = '''INSERT INTO sleep_table
                                        (hours, date)
                                        VALUES (?, ?);'''
            cursor.execute(insert_data_command, data)
            db.commit()
            db.close()

            print(f'''The DB has been successfully updated with new data:\n
                    hours : {hr}
                    date : {dt}\n''')
        except sqlite3.Error as e:
            print(f'Failed to update the DB. An error occurred:\n', e)
    else:
        print(f'The record for the date - {dt} - already exists, or has incorrect format.')

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
        print(f'Failed to process the DB records. An error occurred:\n', e)






# Initialize the database (executed only once, or when to reset the DB).
#init_db()

# Display all the database records.
#print_records_db()

# test
#randomDate = datetime.datetime.today().strftime('%d/%m/%Y')
#print(type(randomDate))

#update_db(7.0, '32/01/2022')
print_records_db()