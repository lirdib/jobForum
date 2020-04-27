import os.path
class worker:
    def __init__(self, name, password):  # Each worker will have a name
        self.name = name
        self.password = password

    def login(self, f_name):  # f_name is the name of the file.
        login_file = open(f_name, "r")
        data = login_file.readline()
        test = self.name + "." + self.password
        if test != data:
            print("Error")
        else:
            print("You are loged in")

class employer:
    def __init__(self, name, password):
        self.name = name
        self.password = password
    def login(self, f_name):  # f_name is the name of the file.
        login_file = open(f_name, "r")
        data = login_file.readline()
        test = self.name + "." + self.password
        if test != data:
            print("Error")
        else:
            print("You are loged in")
    def make_a_new_offer(self):
        print("Please enter the field of your job offer ----1.Electronics,2.Finance,3.Mechanics:")
        type = int(input())
        w, h = 8, 5
        self.electronic = [[0 for x in range(w)] for y in range(h)]# First column would be company name and second wage
        self.finance =[[0 for x in range(w)] for y in range(h)]
        self.mechanics =[[0 for x in range(w)] for y in range(h)]
        if type==1:
            print("Please enter the company name:")
            self.company=input()
            print("Please enter your wage:")
            self.wage = int(input())
            self.electronic[0][0]= self.wage
            self.electronic[0][1]=self.company
            print(self.electronic[0][0])
            global fn
            fn = self.name+"jobs.txt"
            fi = open(fn,"w")
            fi.write(str(self.electronic[0][0])+"."+str(self.finance[0][1]))
            fi.close()
        if type==2:
            print("Please enter the company name:")
            self.company=input()
            print("Please enter your wage:")
            self.wage = int(input())
            self.finance[0][0]= self.wage
            self.finance[0][1]=self.company
            print(self.electronic[0][0])
            fi = open(fn,"w")
            fi.write(str(self.finance[0][0])+"."+str(self.finance[0][1]))
            fi.close()
        if type == 3:
            print("Please enter the company name:")
            self.company = input()
            print("Please enter your wage:")
            self.wage = int(input())
            self.mechanics[0][0] = self.wage
            self.mechanics[0][1] = self.company
            print(self.electronic[0][0])
            fi = open(fn, "w")
            fi.write(str(self.mechanics[0][0]) + "." + str(self.mechanics[0][1]))
            fi.close()
    def print_offers(self):
        f_name = self.name+"jobs.txt"


       

print("---Welcome to the job forum---\n Please press 1 to search for job, 2 to post a job offer, press 3 to exit")
choice = int(input())
global login_flag
login_flag = False
if choice == 1:
    ch = int(input("Press 1 to Sign in or 2 to Log in "))
    if ch == 1:
        name = input("Please enter you name:")
        password = input("Please enter you password")
        file_name = name + ".txt"
        signin_file = open(file_name, "w")  # Write name and passowrd to a file
        signin_file.write(name + "." + password)
        signin_file.close()
        global flag
        flag = True
    if ch == 2:
        global namee
        namee = input("Please enter you name:")
        global passs
        passs = input("Please enter you password")
        fileName = namee + ".txt"
        if os.path.exists(fileName):  # Check if this user is registered
            worker1 = worker(namee, passs)# Create the constructor for worker class
            worker1.login(fileName)
            # This flag shows if it is a worker or an employer
            flag = True
            login_flag = True
if choice == 2:
    ch = int(input("Press 1 to Sign in or 2 to Log in"))
    if ch == 1:
        name = input("Please enter you name:")
        password = input("Please enter you password")
        file_name = name + ".txt"
        signinemployer_file = open(file_name, "w")  # Write name and passowrd to a file
        signinemployer_file.write(name + "." + password)
        signinemployer_file.close()
        flag = False
    if ch == 2:
        name = input("Please enter you name:")
        pas = input("Please enter you password")
        fName = name + ".txt"
        if os.path.exists(fName):  # Check if this user is registered
            employerA = employer(name, pas)# Create the constructor for emplyer class
            employerA.login(fName)
            flag = False
            login_flag = True

if choice == 3:
    print(quit)
    quit()

if login_flag == True:
    if flag == False: #Employer
        print("Press 1 to make a new offer, press 2 to see other offers, press 3 to get back to menu")
        c= int(input())
        if c == 1:
            employerA.make_a_new_offer()

            
            
