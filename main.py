from task_manager import add_task, remove_task, list_tasks
from storage import load_tasks, save_tasks
from utils import print_menu, get_user_choice

def main():
    tasks = load_tasks()

    while True:
        print_menu()
        choice = get_user_choice()

        if choice == "1":
            task = input("Masukkan tugas baru: ")
            add_task(tasks, task)
        elif choice == "2":
            list_tasks(tasks)
            index = int(input("Masukkan nomor tugas yang akan dihapus: ")) - 1
            remove_task(tasks, index)
        elif choice == "3":
            list_tasks(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()
