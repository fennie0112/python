username = "Rahul"

def update():
    global username
    username = input("Enter new username: ")

update()
print("Username =", username)