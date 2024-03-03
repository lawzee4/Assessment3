# load_data.py
import csv
import sqlite3
import logging

# Configure logging
logging.basicConfig(filename='loading_data.log', level=logging.ERROR)

def load_sales_data():
    try:
        conn = sqlite3.connect('walmart_database.db')
        c = conn.cursor()

        with open('data.csv/train.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skips the header row
            for row in reader:
                # Converts IsHoliday to integer (0 or 1)
                is_holiday = 1 if row[4] == 'TRUE' else 0
                # Insert data into the sales table
                c.execute("INSERT INTO sales (Store, Dept, Date, Weekly_Sales, IsHoliday) VALUES (?, ?, ?, ?, ?)",
                          (row[0], row[1], row[2], row[3], is_holiday))
        conn.commit()
    except sqlite3.Error as e:
        logging.error("SQLite error occurred: %s", e)
    except Exception as ex:
        logging.error("An error occurred during sales data loading: %s", ex)
    finally:
        if conn:
            conn.close()

def load_features_data():
    try:
        conn = sqlite3.connect('walmart_database.db')
        c = conn.cursor()

        with open('data.csv/features.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skips the header row
            for row in reader:
                # Insert data into the features table
                c.execute("INSERT INTO features (Store, Date, Temperature, Fuel_Price, MarkDown1, MarkDown2, MarkDown3, MarkDown4, MarkDown5, CPI, Unemployment, IsHoliday) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                          (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11]))
        conn.commit()
    except sqlite3.Error as e:
        logging.error("SQLite error occurred: %s", e)
    except Exception as ex:
        logging.error("An error occurred during features data loading: %s", ex)
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    load_sales_data()
    load_features_data()
