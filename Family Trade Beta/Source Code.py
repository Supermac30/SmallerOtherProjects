"""
 This is the testing phase of family trade. May the force be wih us.
"""

import hashlib
import os

   # the account making protocal
def register():
    while True:
        name = input("type in the username you will you use: \n")
        if CheckNewUser(name) == "Safe":
            break
        else:
            print("Sorry, the username is taken, please input another one,")
    while True:
        password = input("type in the password you will use: \n")
        password2 = input("type in the password again: \n")
        if password == password2:
            break
    password = "b\'" + password + "\'"
    m = hashlib.sha224()
    m.update(eval(password))
    password = m.hexdigest()
    os.chdir(r'.\Database')
    make_new = open("Password Database.txt", "a+")
    make_new.write(",\"" + name + "\" : \"" + password + "\"" )
    make_new.close()
    os.chdir(r'..')
    makeUser(name)
    os.chdir(r'.\Database')
    add = open("User Database.txt", "a+")
    add.write("\n" + name)
    print("registration successful")
    os.chdir(r'..')
    return None


   # the sign in protocal
def signInProcess(Username,done):
    os.chdir(r'.\Database')
    with open("Password Database.txt") as hi:
        data = eval(hi.read() + "}")
        who = input("type in your username: ")
        try:
            passs = data[who]
        except KeyError:
            do_you = input("you are not a registered user do you want to sign up? Y/N \n")
            os.chdir(r'..')
            if do_you.lower() == "y":
                register()
            return None
        time = 0 
        while True:
            time += 1
            shh = input("tell me your password: ")
            shh = "b\'" + shh + "\'"
            m = hashlib.sha224()
            m.update(eval(shh))
            hashpass = m.hexdigest()
            if hashpass == passs:
                print("access granted")
                done = True
                print(done)
                os.chdir(r'..')
                return done, who
            else:
                print("access denied")
            if time % 3 == 0:
                do_you = input("do you want to change the inputed user name? Y/N \n")
                if do_you.lower() == "y":
                    os.chdir(r'..')
                    return None
                    
   #create new users
def makeUser(Name):
    os.chdir(r'.\Users')
    Name = Name + ".txt"
    hi = open(Name,"w+")
    hi.close()
    hi = open(Name, "w")
    hi.write("0")
    hi.close()
    os.chdir(r'..')
    return None

    #checks for a username has been taken
def CheckNewUser(name):
    os.chdir(r'.\Database')
    if str(name) in open('User Database.txt').read():
        os.chdir(r'..')
        return "Taken"
    else:
        os.chdir(r'..')
        return "Safe"
  
   #check the database for registered users
def checkUsers():
    os.chdir(r'.\Database')
    with open("User Database.txt") as s:
        os.chdir(r'..')
        return s.read()

  # Unsecure Trading System, should work on this
def trade(amount,endUser,startUser):
    if int(amount) < 0:    # check if the trading value is under 0
        return "Error"
    os.chdir(r'.\Users')
    startUser = startUser + ".txt"
    check = open(startUser)     #    opening startUsers account
    inside = check.read()
    check.close()
    change = open(startUser,"w") # changing startUsers account
    try:
        hmm = 'y'
        if (int(inside) - int(amount)) < -50:
            hmm = input("you will exceed the maximum debt limit if you do this, are you sure? Y/N")
        elif (int(inside) - int(amount)) < 0:
            hmm = input("you will go into debt if you do this, are you sure? Y/N")
        if hmm.lower() == "n":
            change.write(inside)
            os.chdir(r'..')
            return None
        change.write(str(int(inside) - int(amount)))
    except ValueError or UnboundLocalError:
        print("Sorry an error has occured, please call help desk (Mark)")
    change.close()
    endUser = endUser + ".txt"   
    check = open(endUser)     # opening endUsers account
    inside = check.read()
    check.close()
    change = open(endUser,"w") # changing endUsers account
    try:
        change.write(str(int(amount) + int(inside)))
    except ValueError:
        print("Sorry an error has occured, please call help desk (Mark)")
        change.close()
    if endUser == startUser:
        print("Congrats! You just finished trading with yourself.")
    os.chdir(r'..')
    return None

  # check balance
def checkBalance(username):
    username = username + ".txt"
    os.chdir(r'.\Users')
    with open(username) as f:
        balance = f.read()
    os.chdir(r'..')
    return balance

  # have the user delete their account
def deleteUser(user):
    os.chdir(r'.\Users')
    file = str(user) + '.txt'
    os.remove(file)
    os.chdir(r'..')
    os.chdir(r'.\Database')
    with open("Password Database.txt") as f:
        dictionary = eval(f.read() + "}")
        del dictionary[user]
        f.close()
    with open("Password Database.txt","w") as g:
        dictionary = str(dictionary)[:-1]
        g.write(dictionary)
        g.close
    with open("User Database.txt") as h:
        lines = h.readlines()
        h.close()
    with open("User Database.txt","w") as i:
        for line in lines:
            if line == user + "\n":
                i.write(line)
        i.close()
    os.chdir(r'..')
    return None

def addFinance(user,amount):
    os.chdir(r'.\Users')
    endUser = user + ".txt"   
    check = open(endUser)     # opening endUsers account
    inside = check.read()
    check.close()
    change = open(endUser,"w") # changing endUsers account
    try:
        change.write(str(int(amount) + int(inside)))
    except ValueError:
        print("Sorry an error has occured, please call help desk (Mark)")
        change.close()
    os.chdir(r'..')
    return None

''' variables store start'''
debt_limit = -50
''' variables store end'''

while True:
    done = False
    Username = ""
    while done == False:
        try:
            done, Username = signInProcess(Username,done)
        except TypeError:
            continue

    for i in range(45):
        print("\n")
        
      # User Interface
    what = input("Welcome to family trade, how can I be of assistance? Close / Trade / Balance / Add Finances / Delete User \n")
    while True:
        
        if int(checkBalance(Username)) <= debt_limit: #check if user is past the maximum debt limit
            print("your account privilages have been taken away until your debt has been removed")        

            while int(checkBalance(Username)) <= debt_limit: #traps the user into a loop until debt is removed
                what = input("How can I be of assistance? Close / Balance \n")

                if what.lower() == "balance" :  #check your balance
                    print(checkBalance(Username) + " Family Bucks")
                    
                if what.lower() == "close" :   #close program
                    print("Thank you for using family trade")
                    break
                
        if what.lower() == "balance" :  #check your balance
            print(checkBalance(Username) + " Family Bucks")
            print(str(int(checkBalance(Username)) - debt_limit) + " is left until account privlages are taken away")

        if what.lower() == "add finances" :  #should work on this more
            amount = input("how much do you want to add?")
            addFinance(Username, amount)
            print("You now have " + checkBalance(Username) + " Family Bucks")

        if what.lower() == "close":   #close program
            print("Thank you for using family trade")
            break

        if what.lower() == "trade":   #trade with your friends
            while True:
                who = input("With whom would you like to trade with? \n you can trade with: \n \n" + checkUsers() + "\n")
            
                howMuch = input("How much would you like to trade? \n")
                x = trade(howMuch, who, Username)
                if x == "Error":
                    print("\n you cannot trade this amount of currency \n")
                else:
                    break

        if what.lower() == "deleteuser" or what.lower() == "delete user":  
            sure = input("Are you sure you want to delete your account and all associated data? Y/N")
            if sure.lower() == "y":
                deleteUser(Username)
                print("All data has been removed; Thank You for using Family Trade")
                break
            else:
                continue

        what = input("How can I be of assistance? Close / Trade / Balance / Delete User / Add Finances\n")






"""
   ToDo List:
     - encrypt the online currency
     - finish an add finances option
     - add a GUI
     - integrate networking
"""






