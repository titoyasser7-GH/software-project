from data import user_data

def login():

    while True:
        pin = input("Enter PIN: ")

        if pin == user_data["pin"]:
            print("Login Successful!")
            return True
        else:
            print("Wrong PIN.")

    return False