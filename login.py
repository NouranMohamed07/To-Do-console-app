from Authentication import AuthenticationSystem

if __name__ == "__main__":
    while True:
            choice = input("Do you want to register or login? (register/login): ").strip().lower()
            if choice == "register":
                AuthenticationSystem.register_user()
                break
            elif choice == "login":
                AuthenticationSystem.login_user()
                break
            else:
                print("Invalid choice, try again.")

