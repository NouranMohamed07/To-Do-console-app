import datetime

class TaskNotifications:

    @staticmethod
    def show_notifications(user):
        print("\n Task Notifications ")

        today = datetime.date.today()
        has_notifications = False

        try:
            with open("tasks.txt", "r") as file:
                for line in file:
                    parts = line.strip().split(",")

                    task_title = parts[1]
                    task_status = parts[4]
                    due_date = datetime.datetime.strptime(parts[5], "%Y-%m-%d").date()
                    owner = parts[6]

                    if owner != user["email"] or task_status == "Completed":
                        continue

                    # Overdue Tasks
                    if due_date < today:
                        print(f" Overdue Task: {task_title} (Due: {due_date})")
                        has_notifications = True

                    # Upcoming within 24 hours
                    elif due_date == today + datetime.timedelta(days=1):

                        print(f" Upcoming Task: {task_title} (Due: {due_date})")
                        has_notifications = True

            if not has_notifications:
                print("No notifications 🎉")

        except FileNotFoundError:
            print("No tasks found.")
