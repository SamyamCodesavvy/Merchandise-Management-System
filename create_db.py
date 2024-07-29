import sqlite3

def create_db():
    con = sqlite3.connect(database=r'rmms.db')
    
    cur = con.cursor()
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS employee (
            invoice INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            contact TEXT,
            desc TEXT,
        )
    """)
    con.commit()
    
    con.close()

# Call the function to create the database and table
create_db()
