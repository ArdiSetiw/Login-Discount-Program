# Simpel Program Login dan Register 
print("""\033[32m
     ====================================
    |Simple Login and Registration System|
     ==================================== \033[39m
""")

data = {'Default':'Default'} 
x = 1
print("="*45)
print("> If you already have account type 'Log'\n> If you don't have account type 'Reg'\n> Type 'End' to end the program")
print("="*45)
while x > 0 :   
    x += 1
    choice = str(input("Type here = "))

    # Registration
    if choice == "Reg" or choice == "reg" :
        print("| Registration Procces")
        RegId = str(input("> Username = "))
        RegPw = str(input("> Password = "))
        data[RegId] = RegPw
        print("="*45)
        print("\033[32mRegistration Complete !\033[39m")
        print("="*45)

    # Login
    elif choice == "Log" or choice == "log" :
        print("| Log in Procces")
        y = 1
        while y > 0 :
            id = str(input("> Username = "))
            pw = str(input("> Password = "))
            if id in data and data[id] == pw :
                print("="*45)
                print("\033[32mLog in Succes !\033[39m")
                print("="*45)
                break
            else : 
                print("\033[31mYou have a wrong username or password\033[39m")
                if y >= 3 :
                    print("\033[31mCan't Login anymore cause you have wrong 3 times\033[39m")
                    print("="*45)
                    break
            y += 1

    # End Program
    elif choice == "End" or choice == "end" :
        print("Program Ended")
        print("="*45)
        break
    
    else :
        print("\033[31mPlease type either 'Reg','Log', or 'End'\033[39m")