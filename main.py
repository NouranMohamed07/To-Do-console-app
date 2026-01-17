from Authentication import AuthenticationSystem
from TaskManagementSystem import TaskMangementSystem
from AdminPanel import AdminPanel

def login():
    while True:
        print("\n Welcome to To-Do App ")
        choice = input("Do you want to register or login? (register/login): ").strip().lower()

        if choice == "register":
            AuthenticationSystem.register_user()

        elif choice == "login":
            logged_user = AuthenticationSystem.login_user()

            if logged_user:
                role = logged_user["role"]
                if role == "admin":
                    AdminPanel.panel()  
                else:
                    TaskMangementSystem.main_badge(logged_user)  

                break # exit from loop when the login was successful

        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    login()
    


