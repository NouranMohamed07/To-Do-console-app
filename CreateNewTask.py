import datetime
import uuid


class CreateNewTask:
    @staticmethod
    def create_task(user):
        title = input("Task Title: ").strip()
        description = input("Task Description (optional): ").strip()

        priority = input("Priority (Low / Medium / High): ").strip().lower()
        while priority not in ["low", "medium", "high"]:
            priority = input("Invalid priority, try again: ").strip().lower()

        status = "To-Do"

        while True:
            due_date = input("Due Date (YYYY-MM-DD): ").strip()
            try:
                date_obj = datetime.datetime.strptime(due_date, "%Y-%m-%d")
                if date_obj.date() <= datetime.date.today():
                    print("Date must be in the future")
                else:
                    break
            except:
                print("Invalid date format")
                          


        task_id = str(uuid.uuid4())[:8]

        with open("tasks.txt", "a") as file:
            file.write(f"{task_id},{title},{description},{priority},{status},{due_date},{user['email']}\n")

        print("Task created successfully")