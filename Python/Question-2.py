# Password should have atleast 8 characters
# Password must have atleast one lowercase character, one uppercase character and a special character

def check_password(password):
    if len(password) >= 8:
        return True
    else:
        return False

password = input("Enter a password: ")
if check_password(password):
    print("Password is valid.")
else:
    print("Password is too short.")
