import json
import sqlite3

from models import Entry
from models.mood import Mood


def get_all_entries():
    # Open a connection to the database
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        # This method accepts a MySQL query as a parameter and executes the given query.
        db_cursor.execute("""
        SELECT
            a.id,
            a.concept,
            a.entry,
            a.mood_id,
            l.label mood_label
        FROM Entries a
        JOIN Moods l
            ON l.id = a.mood_id
        """)

        # Initialize an empty list to hold all animal representations
        entries = []

        # Convert rows of data into a Python list
        # The method fetches all (or all remaining) rows of a query result set and returns a list of tuples.
        # Tuples are used to store multiple items in a single variable.
        # mytuple = ("apple", "banana", "cherry")
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            entry = Entry(row['id'],
                          row['concept'],
                          row['entry'],
                          row['mood_id'])

            mood = Mood(row['id'], row['mood_label'])

            entry.mood = mood.__dict__

            entries.append(entry.__dict__)

    # Use `json` package to properly serialize list as JSON
    # json.dumps() function converts a Python object into a json string.
    return json.dumps(entries)

# Function with a single parameter


def get_single_entry(id):
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT 
            a.id,
            a.concept,
            a.entry,
            a.mood_id,
            l.label mood_label
        FROM Entries a
        JOIN Moods l
            ON l.id = a.mood_id
        WHERE a.id = ? 
        """, (id, ))

        data = db_cursor.fetchone()

        entry = Entry(data['id'], data['concept'],
                      data['entry'], data['mood_id'])

        mood = Mood(data['id'], data['mood_label'])

        entry.mood = mood.__dict__

        return json.dumps(entry.__dict__)


def delete_entry(id):
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM entries
        WHERE id = ?
        """, (id, ))


def create_entry(new_entry):
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Entries
            (concept, entry, mood_id)
        VALUES
            (?, ?, ?);
        """, (new_entry['concept'], new_entry['entry'], new_entry['moodId']))

        id = db_cursor.lastrowid

        new_entry['id'] = id

    return json.dumps(new_entry)


def update_entry(id, new_entry):
    with sqlite3.connect("./journalentry.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Entries
            SET
                concept = ?,
                entry = ?,
                mood_id = ?
        WHERE id = ?
        """, (new_entry['concept'], new_entry['entry'], new_entry['mood_id'], id, ))

        row_affected = db_cursor.rowcount

    if row_affected == 0:
        return False
    else:
        return True
