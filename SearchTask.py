class SearchTask:

    @staticmethod
    def search_tasks(user):
        keyword = input("Enter task title: ").lower()

        with open("tasks.txt", "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if parts[6] == user["email"] and keyword in parts[1].lower():
                    print(f"ID: {parts[0]} \ntitle: {parts[1]} \nstate: {parts[4]} \nDue: {parts[5]} \nPriority: {parts[3]}")
