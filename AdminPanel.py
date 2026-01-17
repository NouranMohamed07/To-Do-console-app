class AdminPanel:

    @staticmethod
    def panel():
        """Admin-only operations"""
        while True:
            print("\nAdmin Panel")
            print("1. Show all users")
            print("2. Show all tasks")
            print("3. Activate a user")
            print("4. Deactivate a user")
            print("5. Delete any task")
            print("6. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                try:
                    with open("users.txt", "r") as file:
                        for line in file:
                            u = line.strip().split(",")
                            print(f"ID: {u[0]}, Name: {u[1]} {u[2]}, Email: {u[3]}, Status: {u[6]}, Role: {u[7]}")
                except FileNotFoundError:
                    print("No users found.")

            elif choice == "2":
                try:
                    with open("tasks.txt", "r") as file:
                        for t in file:
                            t_parts = t.strip().split(",")
                            print(f"ID: {t_parts[0]}, Title: {t_parts[1]}, Status: {t_parts[4]}, Owner: {t_parts[6]}")
                except FileNotFoundError:
                    print("No tasks found.")

            elif choice in ["3", "4"]:
                user_id = input("Enter user ID: ").strip()
                new_status = "active" if choice == "3" else "inactive"
                AdminPanel.change_user_status(user_id, new_status)

            elif choice == "5":
                task_id = input("Enter task ID to delete: ").strip()
                AdminPanel.delete_task(task_id)

            elif choice == "6":
                print("Goodbye Admin ")
                break
            else:
                print("Invalid choice")

    @staticmethod
    def change_user_status(user_id, new_status):
        try:
            with open("users.txt", "r") as file:
                lines = file.readlines()
            with open("users.txt", "w") as file:
                updated = False
                for line in lines:
                    u = line.strip().split(",")
                    if u[0] == user_id:
                        u[6] = new_status
                        updated = True
                    file.write(",".join(u) + "\n")
                if updated:
                    print(f"User {user_id} set to {new_status}")
                else:
                    print("User ID not found")
        except FileNotFoundError:
            print("No users found")

    @staticmethod
    def delete_task(task_id):
        try:
            with open("tasks.txt", "r") as file:
                lines = file.readlines()
            with open("tasks.txt", "w") as file:
                for line in lines:
                    t = line.strip().split(",")
                    if t[0] != task_id:
                        file.write(line)
            print(f"Task {task_id} deleted")
        except FileNotFoundError:
            print("No tasks found")
