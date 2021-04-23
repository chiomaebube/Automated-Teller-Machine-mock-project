import datetime
import random

database = {}

def init():

    correctOptionisselected = False
    print('You are welcome to Mybank plc')

    while correctOptionisselected == False:

        accVerification = input('Do you have an account with us? Type 1(Yes) or 2(No)\n')
        if(accVerification == 1):
            correctOptionisselected = True
            login()

        elif(accVerification == 2):
            correctOptionisselected = True
            print(register())

        else:
            print("Please try again; enter 1 or 2 next time") 

def login():
    print('Please enter your details to login')

    loginSuccessful = False

    while loginSuccessful == False:
   
        username = input("What is your username?\n")
        password = input("Enter your password:\n")
           
        for userDetails in database.items():
            if (userDetails[1] == username):
                if(password[3] == password):

                    print("What's up %s" % username)
                    loginSuccessful = True

                    dT = datetime.datetime.now()

                    print ("Today's date:  = %s/%s/%s" % (dT.day, dT.month, dT.year))
                    print ("The time is now: = %s:%s" % (dT.hour, dT.minute))
                   

                else:
                    print("Password incorrect, please try again")

            else:
                print("Name not found, try again")
    bankOperation(userDetails)

def register():
    print('Please enter your details to login\n\n')

    Fullname = input('Enter your full name, First name first\n')
    username = input('Enter your preferred username\n')
    email = input('Enter your email\n')
    password = input('Enter your password\n')

    accNumber = GenAcctNum()

    database[accNumber] = [ Fullname, username, email, password ]
    print("Your account has been created")
    print("Here's your account number" + accNumber)

   # return database

    login()
   
def bankOperation(user):
    currentbalance = 0.00
    print("Welcome %s, what will you like to do today?" % user[0])
    print("1. Withdrawal" )
    print("2. Cash Deposit")
    print("3. Complaint")

    selectedOption = int(input("Please selcect an option i.e 1:\n"))

    if (selectedOption == 1):
        print("You want to Withdraw!")
        amountToWithdraw = int(input(" How much would you like to withdraw\n"))
        balanceRemaining = currentbalance - amountToWithdraw
        print("Recieved")
        print("Take your cash" + balanceRemaining)

    elif (selectedOption == 2):
        print("You want to Deposit Cash!")
        amountToDeposit = float(input("How much would you like to deposit?\n"))
        currentbalance += amountToDeposit
        print("Your account ballance is now ",currentbalance)


    elif (selectedOption == 3):
        print("You want to Complain!")
        issue = input("What issue will you like to report?\n") 
        print("TComplaint recieved!")
        print("Thank you for contacting us")


    else:
        print("Invalid option selected, please try again")

def GenAcctNum():

    print("Account number loading...\n\n")
    return random.randrange(0000000000, 9999999999)
  

#### BANKING SYSTEM STARTS ####

init()