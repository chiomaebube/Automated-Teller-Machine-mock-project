import datetime
import random

database = {}


def init():
    print('You are welcome to Mybank plc')
    accVerification = int(input('Do you have an account with us? Type 1(Yes) or 2(No)\n'))
    if (accVerification == 1):

        login()

    elif (accVerification == 2):

        print(register())

    else:
        print("Please try again; enter 1 or 2 next time")
        init()


def login():
    print('Please enter your details to login\n')
    print("===========================================\n")

    username = input("What is your username?\n")
    password = input("Enter your password:\n")

    for accNumber, userDetails in database.items():

        if (userDetails[2] == username):
            if (userDetails[4] == password):

                print("What's up %s" % userDetails[0])

                dT = datetime.datetime.now()

                print("Today's date:  = %s/%s/%s" % (dT.day, dT.month, dT.year))
                print("The time is now: = %s:%s" % (dT.hour, dT.minute))

                bankOperation(userDetails)



            else:
                print("Password incorrect, please try again")
                login()

        else:
            print("Name not found, try again")
            login()


def register():
    print('Please enter your details to login\n\n')

    firstName = input("Enter your First name, \n")
    lastName = input("Enter your Last name, \n")
    username = input("Enter your preferred username\n")
    email = input("Enter your email\n")
    password = input("Enter your password\n")

    accNumber = genAcctNum()

    database[accNumber] = [firstName, lastName, username, email, password]
    print("Your account has been created")
    print("Here's your account number %s\n" % accNumber)

    # return database

    login()


def bankOperation(user):
    print("What will you like to do today?\n")
    print("1. Withdrawal")
    print("2. Cash Deposit")
    print("3. Complaint")
    print("4. Logout")

    selectedOption = int(input("Please selcect an option i.e 1:\n"))

    if (selectedOption == 1):
        print("You want to Withdraw!")
        withdrawal()


    elif (selectedOption == 2):
        print("You want to Deposit Cash!")
        deposit()

    elif (selectedOption == 3):
        print("You want to Complain!")
        complain()

    elif (selectedOption == 4):
        logout()
    else:

        print("Invalid option selected, please try again")
        bankOperation(user)


def genAcctNum():
    print("Account number loading...\n\n")
    return random.randrange(0000000000, 9999999999)


def withdrawal():
    currentbalance = 0.00
    amountToWithdraw = int(input(" How much would you like to withdraw\n"))
    balanceRemaining = currentbalance - amountToWithdraw
    balanceRemaining == currentbalance
    print("Recieved")
    print("Take your cash %s" % balanceRemaining)
    logout()


def deposit():
    currentbalance = 0.00
    amountToDeposit = float(input("How much would you like to deposit?\n"))
    currentbalance += amountToDeposit
    print("Your account balance is now %s " % currentbalance)
    logout()

def complain():
    issue = input("What issue will you like to report?\n")
    print("Complaint received!")
    print("Thank you for contacting us")
    logout()



def logout():
   confirm = int(input("Do You want to Logout? 1(Yes) 2(No)\n"))

   if confirm == 1:
       print("Bye!!")

   elif confirm == 2:
        print("Okay!") 
        login()

   else:
        print("please enter 1 or 2")
        logout()



#### BANKING SYSTEM STARTS ####

init()