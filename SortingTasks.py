class SortingTasks:

    @staticmethod
    def sort_tasks(user):
        print("\n Sort Tasks By ")
        print("1. Due Date")
        print("2. Priority")
        print("3. Status")

        choice = input("Enter choice: ").strip()

        try:
            with open("tasks.txt", "r") as file:
                tasks = []
                for line in file:
                    parts = line.strip().split(",")
                    if parts[6] == user["email"]:
                        tasks.append(parts)

            if choice == "1":
                tasks.sort(key=lambda x: x[5])  # Due Date
            elif choice == "2":
                priority_order = {"Low": 1, "Medium": 2, "High": 3}
                tasks.sort(key=lambda x: priority_order.get(x[3], 0))
            elif choice == "3":
                tasks.sort(key=lambda x: x[4])  # Status
            else:
                print("Invalid choice")
                return

            print("\n Sorted Tasks ")
            for task in tasks:
                print(f"ID: {task[0]}  - Title: {task[1]}  -  Status: {task[4]}  -  Due: {task[5]}  -  Priority: {task[3]}\n")

        except FileNotFoundError:
            print("No tasks found")
