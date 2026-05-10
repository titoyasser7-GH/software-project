from enter import login
from transactions import menu

print("=== Welcome to ATM ===")

if login():
    menu()
else:
    print("Too many wrong attempts.")