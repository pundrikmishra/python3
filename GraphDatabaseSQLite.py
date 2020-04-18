import sqlite3
import time
import datetime
import random
from matplotlib import pyplot as plt 
import matplotlib.dates as mdates
# from matplotlib import style
# style.use('fivethirtyeight')



conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS pm(unix REAL, datestamp TEXT, keyboard TEXT, value REAL)')


def data_entry():
    c.execute("INSERT INTO pm VALUES(112789233, '2020-05-18', 'MehtaJi',750000000)")
    conn.commit()
    c.close()
    conn.close()

def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%y-%m-%d %H:%M:%S'))
    keyword = 'python'
    value = random.randrange(0, 10)
    c.execute("INSERT INTO pm (unix, datestamp, keyboard, value) VALUES (?,?,?,?)",(unix,date,keyword,value))
    conn.commit()

def read_from_db():
    # c.execute('SELECT * FROM pm')
    # c.execute("SELECT * FROM pm WHERE value=3 AND keyboard ='python'")
    # c.execute("SELECT keyboard, unix, value,datestamp FROM pm WHERE value=3 AND keyboard ='python'")
    c.execute("SELECT keyboard, unix FROM pm WHERE value=3 AND keyboard ='python'")
    # data= c.fetchall()
    # print(data)
    for row in c.fetchall():
        print(row)
        # print(row[0])

def graph_data():
    c.execute('SELECT datestamp, value FROM pm')
    dates = []
    values = []
    for row in c.fetchall():
        # print(row)
        # dates.append(datetime.datetime.fromtimestamp(row[0]))

        dates.append(row[0])
        values.append(row[1])
    plt.plot_date(dates , values, '_' )
    plt.show()

 
# create_table()
# data_entry()
# for i in range(10):
#     dynamic_data_entry()
#     time.sleep(1)
# read_from_db()
graph_data()
c.close()
conn.close()

