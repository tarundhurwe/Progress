import sqlite3 as sql
import json
from os.path import dirname, join


def upload_data(json_file):
    with open(json_file, "r") as f:
        json_data = json.loads(f.read())

    conn = sql.connect(join(dirname(__file__), "../backend/db.sqlite3"))
    cur = conn.cursor()
    try:
        for index, data in enumerate(json_data):
            problem_type, name, problem_link = data
            cur.execute(
                "INSERT INTO api_problem (problem_name, problem_link, problem_set_id_id, problem_difficulty, problem_type) VALUES (?, ?, ?, ?, ?)",
                (name, problem_link, 1, "Easy", problem_type),
            )
            conn.commit()
        conn.close()
    except Exception as e:
        print(f"Error: {e}")


path = join(dirname(__file__), "./dsa450.json")
upload_data(path)

# ('api_note',), ('api_problemlist',), ('api_problem',), ('django_content_type',), ('auth_permission',), ('auth_group',), ('auth_user',), ('django_session',), ('api_status',)
