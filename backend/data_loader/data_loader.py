from os.path import join, dirname
import json
import sqlite3 as sql


def load_data(json_file_name, problem_set_name):
    with open(json_file_name, "r") as json_file:
        json_data = json.load(json_file)
    connection = sql.connect(join(dirname(__file__), "../db.sqlite3"))
    c = connection.cursor()
    k = c.execute(
        f"""SELECT problem_set_id FROM api_problemlist where problem_set_name = '{problem_set_name}'"""
    )
    problem_set_id = k.fetchone()[0]
    for data in json_data:
        problem_name, problem_type, difficulty, link = data
        try:
            c.execute(
                f"""INSERT INTO api_problem (problem_set_id_id, problem_name, problem_type, problem_difficulty, problem_link) VALUES ({problem_set_id}, '{problem_name}', '{problem_type}', '{difficulty}', '{link}')"""
            )
            connection.commit()
            print("Data inserted successfully")
        except Exception as e:
            print(f"ERROR: {e}")


load_data("problem.json", "Blind 75")
