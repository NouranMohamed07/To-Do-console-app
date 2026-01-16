class DeleteTask:
        
    @staticmethod
    def delete_task(user):
        task_id = input("Enter Task ID: ").strip()

        with open("tasks.txt", "r") as file:
            lines = file.readlines()

        with open("tasks.txt", "w") as file:
            for line in lines:
                parts = line.strip().split(",")
                if not (parts[0] == task_id and parts[6] == user["email"]):
                    file.write(line)

        print("Task deleted")
