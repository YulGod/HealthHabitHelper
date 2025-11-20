from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to HealthHabitHelper (HHH) - Minimalist Health Tracker"

if __name__ == '__main__':
    app.run(debug=True)