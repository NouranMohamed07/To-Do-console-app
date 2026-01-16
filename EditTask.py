import datetime


class EditTask:

    @staticmethod
    def edit_task(user):
        task_id = input("Enter Task ID: ").strip()

        with open("tasks.txt", "r") as file:
            lines = file.readlines()

        updated = False
        with open("tasks.txt", "w") as file:
            for line in lines:
                parts = line.strip().split(",")

                if parts[0] == task_id and parts[6] == user["email"]:
                    print("1. Change Title")
                    print("2. Change Description")
                    print("3. Change Priority")
                    print("4. Mark as Completed")
                    print("5. Change due to date")

                    choice = input("Enter choice: ")

                    if choice == "1":
                        parts[1] = input("New Title: ")
                    elif choice == "2":
                        parts[2] = input("New Description: ")
                    elif choice == "3":
                        parts[3] = input("New Priority (Low/Medium/High): ")
                    elif choice == "4":
                        parts[4] = "Completed"
                    elif choice == "5":
                        while True:
                            try:
                                new_date = input("New Due Date (YYYY-MM-DD): ").strip()
                                date_obj = datetime.datetime.strptime(new_date, "%Y-%m-%d")

                                if date_obj.date() <= datetime.date.today():
                                    print("Date must be in the future")
                                else:
                                    parts[5] = new_date
                                    break
                            except ValueError:
                                print("Invalid date format, try again")


                    updated = True

                file.write(",".join(parts) + "\n")

        if updated:
            print("Task updated successfully")
        else:
            print("Task not found or not yours")
