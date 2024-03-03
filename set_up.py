import sqlite3

conn = sqlite3.connect('walmart_database.db')
c = conn.cursor()


# drop the tables - use this order due to foreign keys - so that we can rerun the file as needed without repeating values
conn.execute('DROP TABLE IF EXISTS sales')
conn.execute('DROP TABLE IF EXISTS features')


# Create sales table
c.execute('''CREATE TABLE sales
             (Date TEXT, Weekly_Sales REAL, Store INTEGER, Dept INTEGER, IsHoliday INTEGER,
             PRIMARY KEY(Store, Dept, Date))''')

# Create features table with foreign key constraints
# Create features table with foreign key constraints
c.execute('''CREATE TABLE features
             (Store INTEGER, Date TEXT, Temperature REAL, Fuel_Price REAL, MarkDown1 REAL,
             MarkDown2 REAL, MarkDown3 REAL, MarkDown4 REAL, MarkDown5 REAL, CPI REAL, Unemployment REAL, IsHoliday INTEGER,
             PRIMARY KEY(Store, Date),
             FOREIGN KEY(Store) REFERENCES sales(Store),
             FOREIGN KEY(Date) REFERENCES sales(Date))''')


# Create indexes
c.execute('''CREATE INDEX idx_sales_date ON sales(Date)''')
c.execute('''CREATE INDEX idx_sales_store ON sales(Store)''')

conn.commit()
conn.close()
