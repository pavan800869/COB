from flask import Flask, url_for, render_template,request, redirect
import sqlite3
from datetime import datetime

app = Flask(__name__)
#Creation database

conn = sqlite3.connect("database.db")
conn.execute('''
    CREATE TABLE IF NOT EXISTS expenses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL,
        amount REAL NOT NULL,
        date TEXT NOT NULL
    )     
''')

conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses ORDER BY date DESC")
    expenses = cursor.fetchall()
    conn.close()
    return render_template("index.html", expenses=expenses)

@app.route('/add', methods=['POST'])
def add_expense():
    description = request.form['description']
    amount = float(request.form['amount'])
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    conn = sqlite3.connect("database.db")
    conn.execute("INSERT INTO expenses (description, amount, date) VALUES(?,?,?)", (description, amount, date))
    conn.commit()
    conn.close()

    return redirect(url_for('index'))

if __name__=="__main__":
    app.run(debug=True)

