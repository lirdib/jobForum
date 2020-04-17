class worker:
    def __init__(self,name,password): # Each worker will have a name
        self.name = name
        self.password = password


class job_offerer:
    pass

print("---Welcome to the job forum---\n Please press 1 to search for job or 2 to post a job offer")
choice = int(input())

if choice == 1:
    ch = input("Press 1 to Log in or 2 to Sign in")
    if ch == 1:
        name=input("Please enter you name:")
        password = input("Please enter you password")
        
