import json
from collections import namedtuple

from pandas import DataFrame

FILE_NAME = "Acc_info.json"
CUSTOMER_DATA = "Customer_info.json"



class Account(object):
    # Initializing the customers attributes
    def __init__(self,first_name,second_name,Dob,address,contact):
        self.__first_name = first_name
        self.__second_name = second_name
        self.__Dob = Dob
        self.__address = address
        self.__contact = contact
        self.__account_number = ""
        self.__pin = ""
        self.__data = namedtuple("Customer_info","first_name second_name Dob address contact")
        self.__main_data = self.__data(self.__first_name,self.__second_name,self.__Dob,self.__address,self.__contact)
    
        
    def get_main_data(self):
        """returns the information of the Customer in tuple
        """
        return self.__main_data


    def __save_customer_info(self,customer_data):
        """saves the customer information in the form of a dic
        """
        with open(CUSTOMER_DATA,"w") as file:
            json.dump(customer_data,file)
    
    def __load_customer_info(self):
        """ load the current customers information 
        """
        try:
            with open(CUSTOMER_DATA,"r") as file:
                data = json.load(file)
                return data
        except:
            return{}


    def __save(self,data):
        """
        This method saves and the holder's information into json file
        """
        with open(FILE_NAME,"w") as file:
            json.dump(data,file)



    def __load(self):
        """
        The method returns the holder's account details in json mode 
        """
        try:
            with open(FILE_NAME,"r") as file:
                data = json.load(file)
            return data
        except:
            return {}

    def _get_account_pin(self,account_number,pin):
        """ geting the account number and pin logins
        """
        self.__account_number = account_number
        self.__pin = pin 
        


    def deposit(self,amount,account_number):
        
        data = self.__load()
        customer_data  = self.__main_data 
        information = self.__load_customer_info()
        
        
        #updating the customers' account
        if (customer_data.first_name in data) and information[customer_data.first_name + " "+ customer_data.second_name][1] ==account_number:
            current_amount = int(data[customer_data.first_name]) + int(amount)
            data[customer_data.first_name] = current_amount
            self.__save(data)
            print("Amount depsoited Sucessfully!")

        elif (customer_data.first_name in data) and  information[customer_data.first_name + " "+ customer_data.second_name][1] !=account_number:
            print("Alert wrong account number!")

        else:
            #saving the info of the new_customer
            data[customer_data.first_name] = int(amount)
            information[customer_data.first_name+" "+customer_data.second_name] = (customer_data,self.__account_number,self.__pin)
            self.__save_customer_info(information)
            # saving the amount deposited 
            self.__save(data)
            print("Deposited Successfully!")


    def withdraw(self,amount,pin):
        customer_info = self.__load_customer_info()
        data = self.__load()
        customer_name = ""
        for key, value in customer_info.items():
            if pin in value:
                customer_name = key.split()[0]
            else:
                print("Incorrect pin!")
            break
        if customer_name in data:
            if int(amount) > int(data[customer_name]):
               print(" Insufficent Funds")

            else:
                new_balance = int(data[customer_name]) - int(amount)
                data[customer_name] = new_balance
                self.__save(data)
                print("Amount withdrawn successffully!")


                    


    def check_balance(self,first_name,second_name,Account_number,pin):
        data = self.__load_customer_info()
        info = self.__load()
        acc_num,pin_1 = data[first_name+ " "+second_name][1],data[first_name+ " "+second_name][2] 
        if Account_number ==acc_num or pin_1 ==pin:
            balance = info[first_name]
            print("Mr",first_name, "your balance is: ${:,}".format(balance))
        else:
            print("An error occured")
        
    def show_transaction(self):
        # use Orderedic to store the info
        # use the reversed for loop to display the time and transactions and the money 
        pass


