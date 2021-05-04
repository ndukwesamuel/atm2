import random
# from databases import Database
from getpass import getpass


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

    if not data:
        try:
            print('wrong account or account does not exis')
            start()

        except:
            print("An exception occurred")
            if user_account_number == data[4]:
                password = input("What is your password \n")
                email =  input("What is your email \n")

                if password == data[3] and email == data[0]:
                    user = data
                    bank_operation(user)

                    print('we move ')

                else:
                    print('we cry')
                    login()
            else:
                print('return back')


def generation_account_number():
    return random.randrange(1111111111, 9999999999)

def bank_operation(user):
    print("Welcome %s %s " % (user[0], user[1]))

    selected_option = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Logout (4) Exit \n"))

    if selected_option == 1:

        deposit_operation()
    elif selected_option == 2:

        withdrawal_operation()
    elif selected_option == 3:

        logout()
    elif selected_option == 4:

        exit()
    else:

        print("Invalid option selected")
        bank_operation(user)

start()