import re
import hashlib
import os
from TaskNotifications import TaskNotifications

class AuthenticationSystem:

    @staticmethod
    def register_user():


        # Collect User Data 
        id_number = validate_id(input("Enter ID Number in 14 digit only: ").strip())
        first_name = input("Enter First Name: ").strip()
        last_name = input("Enter Last Name: ").strip()
        password = input("Enter Password: ").strip()
        hashed_password = confirm_password(password)
        email = validate_email_format(input("Enter Email: ").strip())
        mobile = is_valid_egyptian_mobile(input("Enter Mobile Number: ").strip())
        

        def is_unique_id(id_number):
            try:
                with open("users.txt", "r") as file:
                    for line in file:
                        saved_id = line.strip().split(",")[0]  # assuming ID is first field
                        if saved_id == id_number:
                            return False
            except FileNotFoundError:
                return True
            return True

        def validate_id(id_number):
            while True:
                if not (id_number.isdigit() and len(id_number) == 14):
                    id_number = input("error.Invalid ID number format, try agin in 14 digit: ").strip()
                    continue
                if not is_unique_id(id_number):
                    id_number = input("error. familiar ID, try again with a unique ID: ").strip()
                    continue
                return id_number

        # Confirm password method with hashing password
        def confirm_password(password):
            while True:
                confirm = input("Confirm Password: ").strip()
                if confirm == password:
                    # Hash password
                    salt = os.urandom(16)
                    iterations = 260000
                    pw_hash = hashlib.pbkdf2_hmac(
                        "sha256",
                        password.encode('utf-8'),
                        salt,
                        iterations
                    )
                    stored_hash = f"{iterations}${salt.hex()}${pw_hash.hex()}"
                    return stored_hash
                else:
                    print("error. Passwords do not match, try agin")

        def validate_email_format(email):
            pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            while not re.match(pattern, email):
                email = input("error. Invalid email format, try again: ").strip()
            return email

        def is_valid_egyptian_mobile(number):
            pattern = r"^(010|011|012|015)\d{8}$"
            while not re.fullmatch(pattern, number):
                number = input("error. Invalid phone number, try again: ").strip()
            return number

        def status(state):
            if state == "inactive":
                return "inactive"
            else:
                return "active"

        def role(user_type):
            if user_type == "admin":
                return "admin"
            else:
                return "reguler"

        
        # Determine role and status
        if not AuthenticationSystem.is_admin_exists():
            user_status = "active"
            user_role = "admin"
            print("First user registered as admin and active")
        else:
            user_status = "inactive"
            user_role = "reguler"
            print("User registered as inactive, waiting for admin activation")
        

        user = {
            "id_number": id_number,
            "first_name": first_name,
            "last_name": last_name,
            "password": hashed_password,
            "email": email,
            "mobile": mobile,
            "status": user_status,
            "role": user_role
        }

        # Save User 
        with open("users.txt", "a") as file:
            file.write(",".join([
                user["id_number"],
                user["first_name"],
                user["last_name"],
                user["email"],
                user["password"],
                user["mobile"],
                user["status"],
                user["role"]
            ]) + "\n")

        print("\nUser registered successfully!")
        for key, value in user.items():
            if key != "password":
                print(f"{key}: {value}")

        return user

    @staticmethod
    def login_user():
        print(" User Login ")
        while True:
            email = input("Enter your Email: ").strip()
            password = input("Enter your Password: ").strip()

            try:
                with open("users.txt", "r") as file:
                    found = False
                    for line in file:
                        parts = line.strip().split(",")
                        id_number, first_name, last_name, user_email, stored_password, mobile, user_status, user_role = parts

                        if email == user_email:
                            found = True
                            if user_status != "active":
                                print("error, User is not active. Cannot log in.")
                                break

                            # Verify password
                            iterations, salt, pw_hash = stored_password.split("$")
                            salt = bytes.fromhex(salt)
                            expected_hash = bytes.fromhex(pw_hash)
                            check_hash = hashlib.pbkdf2_hmac(
                                "sha256",
                                password.encode("utf-8"),
                                salt,
                                int(iterations)
                            )

                            if check_hash == expected_hash:
                                print(f"Login successful. Welcome {first_name}!")
                                
                                TaskNotifications.show_notifications({"email": user_email})

                                return {
                                    "id_number": id_number,
                                    "first_name": first_name,
                                    "last_name": last_name,
                                    "email": user_email,
                                    "mobile": mobile,
                                    "status": user_status,
                                    "role": user_role
                                }
                                
                            else:
                                print("error. Wrong password try again")
                                break

                    if not found:
                        print("error, User not found try again")

            except FileNotFoundError:
                print(" No users registered yet.")
                return AuthenticationSystem.register_user()


    @staticmethod
    def is_admin_exists():
        try:
            with open("users.txt", "r") as file:
                for line in file:
                    if ",admin" in line:
                        return True
        except FileNotFoundError:
            return False
        return False


    
