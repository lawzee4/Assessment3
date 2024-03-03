import csv
import sqlite3
import logging

# Configure logging
logging.basicConfig(filename='loading_data.log', level=logging.ERROR)

def load_sales_data():
    try:
        conn = sqlite3.connect('walmart_database.db')
        c = conn.cursor()

        with open('sales.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skips the header row
            for row in reader:
                # Converts IsHoliday to integer (0 or 1)
                is_holiday = 1 if row[4] == 'TRUE' else 0
                c.execute("INSERT INTO sales (Date, Weekly_Sales, Store, Dept, IsHoliday) VALUES (?, ?, ?, ?, ?)",
                          (row[2], row[3], row[0], row[1], is_holiday))
        conn.commit()
    except sqlite3.Error as e:
        logging.error("SQLite error occurred: %s", e)
    except Exception as ex:
        logging.error("An error occurred during data loading: %s", ex)
    finally:
        if conn:
            conn.close()

def load_features_data():
    try:
        conn = sqlite3.connect('walmart_database.db')
        c = conn.cursor()

        with open('features.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skips the header row
            for row in reader:
                c.execute("INSERT INTO features (Store, Date, Temperature, Fuel_Price, MarkDown1, MarkDown2, MarkDown3, MarkDown4, MarkDown5, CPI, Unemployment) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                          (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))
        conn.commit()
    except sqlite3.Error as e:
        logging.error("SQLite error occurred: %s", e)
    except Exception as ex:
        logging.error("An error occurred during data loading: %s", ex)
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    load_sales_data()
    load_features_data()
