import json
import sqlite3

from models.mood import Mood


def get_all_moods():
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT 
            a.id,
            a.label
        FROM Moods a
        """)

        moods = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            mood = Mood(row['id'], row['label'])

            moods.append(mood.__dict__)

    return json.dumps(moods)

def get_single_mood(id):
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT 
            a.id,
            a.label
        FROM Moods a
        """, (id, ))

        data = db_cursor.fetchone()

        mood = Mood(data['id'], data['label'])

    return json.dumps(mood.__dict__)
