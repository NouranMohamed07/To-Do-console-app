from CreateNewTask import CreateNewTask
from view_tasks import ViewTasks

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
                    pass

                elif choice == "4":
                    pass

                elif choice == "5":
                    pass

                elif choice == "6":
                    pass

                elif choice == "7":
                    pass

                elif choice == "8":
                    print("Admin logged out")
                    exit()

                else:
                    print("Invalid choice try again")



