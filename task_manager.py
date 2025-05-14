def add_task(tasks, task):
    tasks.append(task)
    print(f"Tugas '{task}' berhasil ditambahkan.")

def remove_task(tasks, index):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"Tugas '{removed}' berhasil dihapus.")
    else:
        print("Indeks tidak valid.")

def list_tasks(tasks):
    if not tasks:
        print("Tidak ada tugas.")
    else:
        print("Daftar Tugas:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")
