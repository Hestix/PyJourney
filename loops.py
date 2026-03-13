username = input("Enter your username:")

if len(username) > 12:
    print("Username must not be gretaer than 12 characters")
elif not username.find(" ") == -1:
    print("Username must not contain spaces")
elif not username.isalpha(): 
    print("Username must not contain digits")
else:
    print(f"Hello {username}")