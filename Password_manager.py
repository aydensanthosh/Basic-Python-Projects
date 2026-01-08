master_pass="Alpha"
def create_password_file():
    with open("password.txt","w") as f:
        f.write(f"{'Username':^20}|{'Password':^20}\n")
        f.write("-"*50+"\n")
create_password_file()
def add(username,password):
    with open("password.txt", "a") as f:
        f.write(f"{username:^20}|{password:^20}\n")
    
def view():
    with open("password.txt","r") as f:
        for line in f.readlines():
            print(line)
Verify=input("What is the master password to this app: ")
if Verify==master_pass:
    while True:
        mode=input("Do you want to Add or View all passwords?(Add/View) or type Q to Quit: ").lower()
        if mode=="add":
            username=input("Enter the username: ")
            password=input("Enter the Password: ")
            add(username,password)
        elif mode=="view":
            view()
        elif mode=="q":
            quit()
        else:
            print("Error:Invalid Option")
        pass
else:
    print("Good try Hacker! Better luck next time.")