import sqlite3

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyboard TEXT, value REAL)')


def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(112789233, '2020-05-18', 'MehtaJi',750000000)")
    conn.commit()
    c.close()
    conn.close()

create_table()
data_entry()