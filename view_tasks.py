class ViewTasks:

    @staticmethod
    def view_tasks(user):
        print("\n My Tasks ")
        try:
            with open("tasks.txt", "r") as file:
                for line in file:
                    parts = line.strip().split(",")
                    if parts[6] == user["email"]:
                        print(f"ID: {parts[0]} \ntitle: {parts[1]} \nstate: {parts[4]} \nDue: {parts[5]} \nPriority: {parts[3]}")
        except FileNotFoundError:
            print("No tasks found")
