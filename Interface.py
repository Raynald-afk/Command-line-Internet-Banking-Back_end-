from CustomerInfo import Account_info, Account_pin_gen
from BankingSystem import Account
import json
import os

def Sign_in():
    """
    This function takes in the required information from the user 
    and returns all the information to the Sign_in_process function 
    """
    print("Please provide correct information to create your account.")
    user = input("Press Enter to continue or stop to exit\n")

    if user.lower() == "stop":
        exit
    else:
        first_name = input("1.Enter your first name (if any)\t")
        second_name = input("2.Enter your second name(if any)\t")
        Dob = input("3.Enter your date of Birth in this format(DD/MM/YY)\t")
        address = input("4.Enter your home address\t")
        contact = input("5.Enter your contact number\t")
        #printing out the info before storing it.

        print("\t\t\t Your information")
        print(f"1.First Name: {first_name}\n2.Second Name: {second_name}\n3.Dob:{Dob}\n4.Address: {address}\n5.Contact Info: {contact}")
        num = input("Press Enter to save! or 'm' to modify the information.")
        # checking if the user will make any changes to the information provided
        while num =="m":
            change  = input("Enter the info number you want to modify (1 -5): ")
            if change =="1":
                first_name - input("Enter your first name (if any)\t")
            elif change == "2":
                second_name = input("Enter your second name(if any)\t")
            elif change == "3":
                Dob = input("Enter your date of Birth in this format(DD/MM/YY)\t")
            elif change == "4":
                address = input("Enter your home address\t")
            elif change == "5":
                contact = input("Enter your contact number\t")
            else:
                num =input("Enter a valid number to make change or press Enter to save: ")
                print()
            #checking if the user will modify any information again 
            print("\t\t\t Your information")
            print(f"1.First Name: {first_name}\n2.Second Name: {second_name}\n3.Dob:{Dob}\n4.Address: {address}\n5.Contact Info: {contact}")
            num = input("Press Enter to save! or 'm' to modify the information.")
        print("Data Saved!")
            
    return first_name ,second_name, Dob,address, contact

def Sign_up_process(first_name,second_name,Dob,address,contact):
        """
        This function is repsonsible for the sign in process of the
        new customer
        """
        info = Account_info(first_name,second_name,Dob,address,contact)

        
        # Generating the new_user's account number and pin
        Account_number,pin = Account_pin_gen()
        print(f"""Hy {info.first_name},
                You have Succefully set up your account. Please take note of the details below.
                1. Account number: {Account_number}
                2. Pin: {pin}
                
                NOTE : This information should not be shared to anyone without your consent.          
                                                                """)
        trader = Account(info.first_name,info.second_name,info.Dob,info.address,info.contact)
        trader._get_account_pin(Account_number,pin)
        
        print("You need to make an intial amount deposit in order to activate your account:")
        amount = input("Please Enter the amount below:\n")
        acc_number = input("Please Enter your account number below:\n")
        trader.deposit(amount,acc_number)
        


def log_in():
    def AccessCheck(data):            

        attempt = 3     
        while attempt >= 1:
            user_id = input("Enter User Name: ")
            password = input("Enter Pin: ")
            for key,value in data.items():
                if user_id in key:
                    if password == value[-1]:
                        first_name,second_name,Dob,address,contact = value[0]
                        customer = Account(first_name,second_name,Dob,address,contact)
                        attempt = 1
                        return True ,customer,first_name ,second_name
                        
                
                    
            print("Incorrect PIn or user_id")
            print(f"Please try again. You have {attempt-1} attempts left!")
            attempt -=1
            if attempt ==0:
                customer = ""
                return False ,customer
            
                

    with open("Customer_info.json","r") as file:
        data  = json.load(file)
        valid,customer,first_name,second_name = AccessCheck(data)
        if valid:
            pass
        else:
            os._exit(0)
                

            
    
                    
    # I have to place This in a functions in order not to call it when it breaks
    boolean = True
    print("\t\t\t\t\t +-------------------------+")
    print("\t\t\t\t\t |        Welcome          |")
    print("\t\t\t\t\t +-------------------------+")
    print()
    while boolean:            
        print("Selection the options below(1-4): ")
        print("1.Deposit Money\n2.Withdraw Money\n3.Check Account Balance\n4.View transaction details")
        option = input("Type here: ")
        if option == "1":
            amount = input("Enter amount to be deposited: ")
            account_number = input("Enter account number to verify: ")
            customer.deposit(amount,account_number)

        elif option =="2":
            amount = input("Type the amount to be redrawm: ")
            pin = input("Enter Pin")
            customer.withdraw(amount,pin)
            print("Money withdrawn Successfully!")
        elif option =="3":
            Account_number = input("Enter your account number: ")
            pin_1 = input("Enter pin: ")
            customer.check_balance(first_name,second_name,Account_number,pin_1)


        boolean = False

        


    

def main():
    print("\t\t\t\t\t +-------------------------+")
    print("\t\t\t\t\t |Welcome to online Banking|")
    print("\t\t\t\t\t +-------------------------+")
    print("Sign up/ Log in \npress '1' to sign in or '2' to log in..")

    user = input()
    while user != "1" and user !="2":
        print("Input Incorrect! Please type in the correct input.")
        user = input("Press '1' to sign in or '2' to log in..\n")
    if user == "1":
        first_name ,second_name, Dob,address, contact = Sign_in()
        Sign_up_process(first_name,second_name,Dob,address,contact)
    if user =="2":
        print("Sign in To Account")
        log_in()
        
main()
    

    
