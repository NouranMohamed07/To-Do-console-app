class FilterTasks:

    @staticmethod
    def filter_tasks(user):
        print("\n Filter Tasks By ")
        print("1. Priority")
        print("2. Status")
        print("3. Due Date")

        choice = input("Enter choice: ").strip()
        filtered_tasks = []

        try:
            if choice == "1":
                value = input("Enter Priority (Low/Medium/High): ").strip().lower()
            elif choice == "2":
                value = input("Enter Status (To-Do/In Progress/Completed): ").strip()
            elif choice == "3":
                value = input("Enter Due Date (YYYY-MM-DD): ").strip()
            else:
                print("Invalid choice")
                return

            with open("tasks.txt", "r") as file:
                for line in file:
                    parts = line.strip().split(",")

                    # Only logged-in user's tasks
                    if parts[6] != user["email"]:
                        continue

                    if choice == "1" and parts[3] == value:
                        filtered_tasks.append(parts)

                    elif choice == "2" and parts[4] == value:
                        filtered_tasks.append(parts)

                    elif choice == "3" and parts[5] == value:
                        filtered_tasks.append(parts)

            if not filtered_tasks:
                print("No tasks match this filter")
                return

            print("\n Filtered Tasks ")
            for task in filtered_tasks:
                print(f"ID: {task[0]} - Title: {task[1]} -  Status: {task[4]}  -  Due: {task[5]}  -  Priority: {task[3]}\n")

        except FileNotFoundError:
            print("No tasks found")
