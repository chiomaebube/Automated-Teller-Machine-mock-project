import datetime

name = input("What is your name?\n")
allowedUsers = ['Chioma', 'Uche', 'Kemi', 'Jide']
allowedPassword = ['passwordChioma', 'passwordUche', 'passwordKemi', 'passwordJide']

if name in allowedUsers:
    password = input("Enter your password:\n")
    userId = allowedUsers.index(name)

    if password in allowedPassword[userId]:

        print("What's up %s" % name)

        dT = datetime.datetime.now()

        print ("Today's date:  = %s/%s/%s" % (dT.day, dT.month, dT.year))
        print ("The time is now: = %s:%s" % (dT.hour, dT.minute))


        print("What will you like to do today?")
        print("1. Withdrawal" )
        print("2. Cash Deposit")
        print("3. Complaint")

        selectedOption = int(input("Please selcect an option i.e 1:\n"))

        if (selectedOption == 1):
            print("You want to Withdraw!")
            amountToWithdraw = int(input(" How much would you like to withdraw\n"))
            print("Recieved")
            print("Take your cash")

        elif (selectedOption == 2):
            print("You want to Deposit Cash!")
            currentbalance = 0.00
            amountToDeposit = float(input("How much would you like to deposit?\n"))
            currentbalance += amountToDeposit
            print("Your account ballance is now ",currentbalance)


        elif (selectedOption == 3):
            print("You want to Complain!")
            issue = input("What issue will you like to report?\n") 
            print("Complaint recieved!")
            print("Thank you for contacting us")


        else:
            print("Invalid option selected, please try again")

    else:
        print("Password incorrect, please try again")

else:
    print("Name not found, try again")
