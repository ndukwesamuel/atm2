import random
# from databases import Database
from getpass import getpass


def ba():
    balance = 1000000
    return balance
data = []

def start():
    print("Welcome to bankPHP")

    have_account = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))

    if have_account == 1:

        login()

    elif have_account == 2:

        register()

    else:
        print("You have selected invalid option")
        start()


def register():
    
    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = getpass("Create a password for yourself \n")


    account_number = generation_account_number()

    data.append(email)
    data.append(first_name)
    data.append(last_name)
    data.append(password)
    data.append(account_number)


    if len(data) == 5:
        print(f'account activated account number={account_number} ')
        login()

    else:
        print("Something went wrong, please try again")
        register()




def login():
    # print("********* Login ***********")
    user_account_number = int(input("What is your account number? \n"))
    if data:
        if user_account_number == data[4]:
            password = input("What is your password \n")
            email = input("enter you email  \n")
            if password == data[3] and email == data[0]:
                user = data
                bank_operation(user)
                print('correct')
            else:
                login()
                print('wweeewe')

        else:
            login()
            print('cryyy')
       
    else:
        print('wrong account or account does not exis')
        start()

def generation_account_number():
    return random.randrange(1111111111, 9999999999)

def bank_operation(user):
    print(f'welcome {user[1]} {user[2]}')
    selected_option = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Logout \n"))

    if selected_option == 1:
        print('deposit_operation')
        deposit_operation()
    elif selected_option == 2:
        print('withdrawal_operation')
        withdrawal_operation()
    elif selected_option == 3:
        print(logout)
        # logout()
    else:
        print("Invalid option selected")
        # bank_operation(user)

def withdrawal_operation():
    print("withdrawal")
    balance_1 = ba()
    withdraw = int(input('enter amount wish to withdraw  \n '))
    if withdraw > balance_1:
        withdrawal_operation()
    else:
        current = balance_1 - withdraw 
        print(f'your current balance is {current} ')
        balance = current
        logout()


    # get current balance
    # get amount to withdraw
    # check if current balance > withdraw balance
    # deduct withdrawn amount form current balance
    # display current balance


def deposit_operation():
    print("Deposit Operations")
    balance_1 = ba()
    print(balance_1)
    deposit = int(input('enter amount wish to deposit \n'))

    current =deposit + balance_1
    print(f'your current balance is {current} ')
    balance_1 = current
    print(balance_1)
    logout()



    # get current balance
    # get amount to deposit
    # add deposited amount to current balance
    # display current balance


def generation_account_number():
    return random.randrange(0,9)
    # 9999999999
    # 1111111111


# def set_current_balance(user_details, balance):
#     user_details[4] = balance


# def get_current_balance(user_details):
#     return user_details[4]

def logout():
    login()

start()