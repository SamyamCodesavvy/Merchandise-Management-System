import sqlite3

def create_db():
    con = sqlite3.connect(database=r'rmms.db')
    
    cur = con.cursor()
    
    cur.execute("""
                CREATE TABLE IF NOT EXISTS employee(
                eid INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT, 
                email TEXT, 
                gender TEXT, 
                contact TEXT, 
                dob TEXT, 
                doj TEXT, 
                pass TEXT, 
                utype TEXT, 
                address TEXT, 
                salary TEXT
                )
                """)

    cur.execute("""
                CREATE TABLE IF NOT EXISTS supplier(
                invoice INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                contact TEXT,
                desc TEXT
                )
                """)

    con.commit()
    con.close()

# Call the function to create the database and tables
create_db()
