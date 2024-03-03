# Walmart Data Explorer

## Introduction

The Walmart Data Explorer is a web application built with Flask, a Python web framework, to facilitate the exploration and visualization of Walmart's sales and features data. The application utilizes an SQLite database to store and retrieve data, providing users with an intuitive interface for analyzing complex datasets.

## Features

### Homepage (`index.html`)

- Welcomes users to the Walmart Data Explorer.
- Directs users to click on links to access specific pages.
- Two links provided:
  - "Sales Page": Redirects to the page displaying Walmart sales data.
  - "Features Page": Redirects to the page displaying Walmart features data.

### Sales Page (`sales.html`)

- Displays sales data in a table format.
- Columns include Date, Weekly Sales, Store, Department, and IsHoliday.
- Users can navigate back to the homepage.

### Features Page (`features.html`)

- Displays features data in a table format.
- Columns include Store, Date, Temperature, Fuel Price, Markdowns, CPI, Unemployment, and IsHoliday.
- Users can navigate back to the homepage.

### Error Handling

- Custom error pages (404 and 500) for a better user experience.
- Detailed logging of errors during data loading for troubleshooting.

## Data Loading Process

The `load_data.py` script reads data from CSV files (`train.csv` and `features.csv`) and inserts it into the SQLite database. The script intelligently converts the 'IsHoliday' column to binary integers (0 or 1) for consistency. Robust exception handling is implemented to manage SQLite errors or unforeseen issues, with detailed error messages logged for diagnostic purposes.

## Database Structure and Indexing

- SQLite database with two tables: `sales` and `features`.
- Tables linked through foreign key constraints for data integrity.
- Indexes (`idx_sales_date` and `idx_sales_store`) created for optimized data retrieval.

## Getting Started

1. Ensure Python and Flask are installed on your system.
2. Open a terminal in the project directory.
3. Set up Flask environment variables:
    ```bash
    export FLASK_APP=app.py
    export FLASK_ENV=development
    ```
4. Initialize the database:
    ```bash
    python database_setup.py
    ```
5. Load data into the database:
    ```bash
    python load_data.py
    ```
6. Start the Flask server:
    ```bash
    flask run
    ```
7. Open a web browser and go to `http://127.0.0.1:5000/` to access the homepage.

## Conclusion

The Walmart Data Explorer is a user-friendly web application that provides a seamless interface for exploring and analyzing Walmart sales and features data. It combines Flask's simplicity, SQLite's reliability, and thoughtful design principles to offer a robust platform for data exploration.