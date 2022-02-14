import sqlite3
from sqlite3 import Error
def sql_connection():
    try:
      conn = sqlite3.connect('Sales.db')
      return conn
    except Error:
      print(Error)
   def sql_table(conn):
    def sql_table(conn):
     cursorObj = conn.cursor()  #Sales.db
    #Current records in salesman table
     cursorObj.execute("SELECT * FROM salesman")
     rows = cursorObj.fetchall()
    print("Agent details:")
     for row in rows:
        print(row)
    print("\nUpdate commission .15 to .45 where id is 5003:")
    sql_update_query = """Update salesman set commission = .45 where salesman_id = 5003"""
      cursorObj.execute(sql_update_query)
    conn.commit()
    print("Record Updated successfully ")
    cursorObj.execute("SELECT * FROM salesman")
    rows = cursorObj.fetchall()
    print("\nAfter updating Agent details:")
    for row in rows:
     print(row)
sqllite_conn = sql_connection()
sql_table(sqllite_conn)
if (sqllite_conn):
  sqllite_conn.close()
  print("\nThe SQLite connection is closed.")
import sqlite3
from sqlite3 import Error
def sql_connection():
    try:
      conn = sqlite3.connect('Sales.db')
      return conn
    except Error:
      print(Error)
def sql_table(conn):
    cursorObj = conn.cursor()  #Sales.db
    #Current records in salesman table
    cursorObj.execute("SELECT * FROM salesman")
    rows = cursorObj.fetchall()
    print("Agent details:")
    for row in rows:
        print(row)
    print("\nUpdate commission .15 to .45 where id is 5003:")
    sql_update_query = """Update salesman set commission = .45 where salesman_id = 5003"""
    cursorObj.execute(sql_update_query)
    conn.commit()
    print("Record Updated successfully ")
    cursorObj.execute("SELECT * FROM salesman")
    rows = cursorObj.fetchall()
    print("\nAfter updating Agent details:")
    for row in rows:
        print(row)
sqllite_conn = sql_connection()
sql_table(sqllite_conn)
if (sqllite_conn):
  sqllite_conn.close()
  print("\nThe SQLite connection is closed.")
import sqlite3
from sqlite3 import Error


def sql_connection():
    try:
        conn = sqlite3.connect('Sales.db')
        return conn
    except Error:
        print(Error)


def sql_table(conn):
    cursorObj = conn.cursor()

    cursor = cursorObj.execute('select * from salesman;')
    print(len(cursor.fetchall()))
    # Insert records
    cursorObj.executescript("""
    INSERT INTO salesman VALUES(5006,'James Hoog', 'New York', 0.15);
    # INSERT INTO salesman VALUES(5007,'Nail Knite', 'Paris', 0.25);
    # INSERT INTO salesman VALUES(5008,'Pit Alex', 'London', 0.15);
    # INSERT INTO salesman VALUES(5009,'Mc Lyon', 'Paris', 0.35);
     # INSERT INTO salesman VALUES(5010,'Paul Adam', 'Rome', 0.45);
        """)
    conn.commit()
    print("\nNumber of records after inserting rows:")
    cursor = cursorObj.execute('select * from salesman;')
    print(len(cursor.fetchall()))


sqllite_conn = sql_connection()
sql_table(sqllite_conn)

if (sqllite_conn):
    sqllite_conn.close()
    print("\nThe SQLite connection is closed.")