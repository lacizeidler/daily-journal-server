import json
import sqlite3
from models.entry import Entry
from models.entry_tags import Entry_Tag
from models.tag import Tag


def get_all_entry_tags():
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT 
            a.id,
            a.entry_id,
            a.tag_id,
            l.concept entry_concept,
            l.entry entry_entry,
            l.mood_id entry_mood_id,
            b.name tag_name
        FROM EntryTag a
        LEFT JOIN Entries l
            ON l.id = a.entry_id
        LEFT JOIN Tags b
            ON b.id = a.tag_id
        """)

        entry_tags = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            entry_tag = Entry_Tag(row['id'], row['entry_id'], row['tag_id'])
            entry = Entry(
                row['id'], row['entry_concept'], row['entry_entry'], row['entry_mood_id'])
            tag = Tag(row['id'], row['tag_name'])

            entry_tag.entry = entry.__dict__
            entry_tag.tag = tag.__dict__
            entry_tags.append(entry_tag.__dict__)

    return json.dumps(entry_tags)


def get_single_entry_tag(id):
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT 
            a.id,
            a.entry_id,
            a.tag_id,
            l.concept entry_concept,
            l.entry entry_entry,
            l.mood_id entry_mood_id,
            b.name tag_name
        FROM EntryTag a
        LEFT JOIN Entries l
            ON l.id = a.entry_id
        LEFT JOIN Tags b
            ON b.id = a.tag_id
        WHERE a.id = ?
        """, (id, ))

        data = db_cursor.fetchone()

        entry_tag = Entry_Tag(data['id'], data['entry_id'], data['tag_id'])
        entry = Entry(
            data['id'], data['entry_concept'], data['entry_entry'], data['entry_mood_id'])
        tag = Tag(data['id'], data['tag_name'])

        entry_tag.entry = entry.__dict__
        entry_tag.tag = tag.__dict__

    return json.dumps(entry_tag.__dict__)


def create_entry_tag(new_entry_tag):
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO EntryTag
            (entry_id, tag_id)
        VALUES 
            (?,?);
        """, (new_entry_tag['entry_id'], new_entry_tag['tag_id']))

        id = db_cursor.lastrowid

        new_entry_tag['id'] = id

    return json.dumps(new_entry_tag)
