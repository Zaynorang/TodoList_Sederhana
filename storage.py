import json
import os

FILENAME = "tasks.json"

def load_tasks():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        json.dump(tasks, f)
    print("Data tugas berhasil disimpan.")
