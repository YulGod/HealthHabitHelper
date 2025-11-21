from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to HealthHabitHelper (HHH) - Minimalist Health Tracker"

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/log/food')
def food_log():
    return "Simple Food Log Feature (Ready)"
# --- Feature: Mood Log (Contributed by Lee Jee Hak) ---
@app.route('/log/mood', methods=['GET', 'POST'])
def mood_log():
    # Deliverable 1: "Provides three simple button options (Good, Normal, Bad)"
    return "Select Today's Mood: [Good] [Normal] [Bad]"