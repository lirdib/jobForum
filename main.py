import os.path
class worker:
    def __init__(self,name,password): # Each worker will have a name
        self.name = name
        self.password = password
    def login(self,f_name,name,password): # f_name is the name of the file.
        login_file = open(f_name, "r")
        data = login_file.readline()
        test = name+"."+password
        if test != data:
            print("Error")
        else:
            print("You are loged in")


class job_offerer:
    pass

print("---Welcome to the job forum---\n Please press 1 to search for job or 2 to post a job offer")
choice = int(input())

if choice == 1:
    ch = int(input("Press 1 to Sign in or 2 to Log in "))
    if ch == 1:
        name=input("Please enter you name:")
        password = input("Please enter you password")
        file_name= name + ".txt"
        signin_file=open(file_name,"w")#Write name and passowrd to a file
        signin_file.write(name+"."+password)
        signin_file.close()
    if ch ==2:
        name = input("Please enter you name:")
        pas = input("Please enter you password")
        fileName = name + ".txt"
        if os.path.exists(fileName):#Check if this user is registered
            worker1 = worker(name,pas)
            worker1.login(fileName,name,pas)
