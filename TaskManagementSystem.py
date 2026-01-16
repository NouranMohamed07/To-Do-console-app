from CreateNewTask import CreateNewTask
from view_tasks import ViewTasks
from EditTask import EditTask
from DeleteTask import DeleteTask
from SearchTask import SearchTask
from SortingTasks import SortingTasks
from FilterTasks import FilterTasks

class TaskMangementSystem:

    def main_badge(logged_user):
        while True:
                print("\n To Do App  ")
                print(f"\n Hello {logged_user['first_name']}  ")
            
                print("1. Create a New Task")
                print("2. View Tasks")
                print("3. Edit Tasks")
                print("4. Delete Tasks")
                print("5. Search Tasks")
                print("6. Sorting Tasks")
                print("7. Filter Tasks")
                print("8. Exit")

                choice = input("Enter your choice: ").strip()

                if choice == "1":
                    CreateNewTask.create_task(logged_user)
                    

                elif choice == "2":
                    ViewTasks.view_tasks(logged_user)

                elif choice == "3":
                    EditTask.edit_task(logged_user)

                elif choice == "4":
                    DeleteTask.delete_task(logged_user)

                elif choice == "5":
                    SearchTask.search_tasks(logged_user)

                elif choice == "6":
                    SortingTasks.sort_tasks(logged_user)

                elif choice == "7":
                    FilterTasks.filter_tasks(logged_user)

                elif choice == "8":
                    print(f"Goodbye {logged_user['first_name']}")
                    exit()

                else:
                    print("Invalid choice try again")



