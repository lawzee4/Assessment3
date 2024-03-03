from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sales')
def display_sales():
    conn = sqlite3.connect('walmart_database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM sales")
    sales_data = c.fetchall()
    conn.close()
    return render_template('sales.html', sales_data=sales_data)

@app.route('/features')
def display_features():
    conn = sqlite3.connect('walmart_database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM features")
    features_data = c.fetchall()
    conn.close()
    return render_template('features.html', features_data=features_data)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
