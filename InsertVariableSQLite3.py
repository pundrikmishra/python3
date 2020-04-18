import sqlite3
import time
import datetime
import random

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS pm(unix REAL, datestamp TEXT, keyboard TEXT, value REAL)')


# def data_entry():
#     c.execute("INSERT INTO pm VALUES(112789233, '2020-05-18', 'MehtaJi',750000000)")
#     conn.commit()
#     c.close()
#     conn.close()

def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%y-%m-%d %H:%M:%S'))
    keyword = 'python'
    value = random.randrange(0, 10)
    c.execute("INSERT INTO pm (unix, datestamp, keyboard, value) VALUES (?,?,?,?)",(unix,date,keyword,value))
    conn.commit()

create_table()
# data_entry()

for i in range(10):
    dynamic_data_entry()
    time.sleep(1)

c.close()
conn.close()

