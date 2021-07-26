import mysql.connector

conn = mysql.connector.connect(
    user = 'root',
    password = 'AktD1KW2YUYSpY3yP60R',
    database='py_db_test'
)

def create_table():
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)')
    conn.commit()

def insert(item, quant, price):
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO store VALUES ('{item}',{quant},{price})")
    conn.commit()

def view():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM store")
    rows = cursor.fetchall()
    return rows

def delete(item):
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM store WHERE item = '{item}'")
    conn.commit()

def update(item, quant, price):
    cursor = conn.cursor()
    cursor.execute(f"UPDATE store SET quantity = '{quant}', price = '{price}' WHERE item = '{item}'")
    conn.commit()

insert('Wine Glass',1,1)
insert('Coffee Cup',50,2)
delete('Wine Glass')
update('Coffee Cup',10,5)
print(view())
conn.close()