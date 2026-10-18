import sqlite3
def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  #lets us access columns by name instead of index
    return conn

DB_NAME = "expenses.db" # in MYSQL it is called database, in SQLite it is called DB file and it is a file that contains the database and creates a table in it and stores the data in it in a structured way and unstructured way as well. It is a file that contains the database and creates a table in it and stores the data in it in a structured way and unstructured way as well. It is a file that contains the database and creates a table in it and stores the data in it in a structured way and unstructured way as well. It is a file that contains the database and creates a table in it and stores the data in it in a structured way and unstructured way as well. It is a file that contains the database and creates a table in it and stores the data in it in a structured way and unstructured way as well. It is a file that contains the database and creates a table in it and stores the data in it in a structured way and unstructured way as well. It is a file that contains the database and creates a table in it and stores the data in it in a structured way and unstructured way as well. It is a file that contains the database and creates a table in it and stores the data in it in a structured way and unstructured way as well. It is a file that contains the database and creates a table in it and stores the data in it in a structured way and unstructured way as well. It is a file that contains the database and creates a table in it and stores the data in it in a structured way and unstructured way as well. It is a file that contains the database and creates a table in it and stores the data in it in a structured way and unstructured way as well. It is a file that contains the database and creates a table in it and stores the data in it in a structured way and unstructured way as well. It is a file that contains the database and creates a table in it and stores the data in it in a structured way and unstructured way as well. It is a file that contains the database and creates a table in it and stores the data in it in a structured way and unstructured way as well. It is a file that contains the database and creates a table in it and stores the data in it in a structured way and unstructured way as well. It is a file that contains the database and creates a table in it and stores the data in it.
def init_db(): # this function will create the database and the table if it doesn't exist
    with get_connection() as conn: # this will create a connection to the database and if the database doesn't exist it will create it and if the table doesn't exist it will create it. with means that the connection will be closed automatically when the block is exited. This is a good practice to avoid memory leaks and to ensure that the connection is closed properly.
                                    # we can use the connection to execute SQL statements and to commit the changes to the database. We can also use the connection to create a cursor object that can be used to execute SQL statements and to fetch the results from the database.
                                    # we are not using a cursor object here because we are not fetching any results from the database. We are only executing SQL statements to create the table and to insert data into the table. We can use the connection object directly to execute SQL statements and to commit the changes to the database.
                                    # we are not write mode and file name inside the get_connection() bcz we are using the DB_NAME variable which contains the file name of the database.but we can use the file name directly inside the get_connection() function if we want to create a different database
                                    # cursor object means a pointer to the database and it is used to execute SQL statements and to fetch the results from the database. It is created by calling the cursor() method of the connection object. We can use the cursor object to execute SQL statements and to fetch the results from the database. We can also use the cursor object to create a new table in the database and to insert data into the table.
        conn.execute("""
                     CREATE TABLE IF NOT EXISTS expenses(
                         id INTEGER PRIMARY KEY AUTOINCREMENT,
                         title TEXT NOT NULL,
                         amount REAL NOT NULL,
                         category TEXT NOT NULL,
                         date TEXT NOT NULL
                     )
                     """)
       
def add_expense(title, amount, category, date)->int:
    with get_connection() as conn:
        cursor = conn.execute("""
                              INSERT INTO expenses(title, amount, category, date) VALUES (?, ?, ?, ?)
                              """, (title, amount, category, date))
        return cursor.lastrowid
   
def get_expenses():
    with get_connection() as conn:
            return conn.execute("SELECT * FROM expenses ORDER BY date DESC").fetchall()
       
def delete_expense(expense_id) -> bool:
    with get_connection() as conn:
        cursor = conn.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
        return cursor.rowcount > 0


# cursor.rowcount ->how many rows were affected by that query


# 123 -> False


# 2 -> True
