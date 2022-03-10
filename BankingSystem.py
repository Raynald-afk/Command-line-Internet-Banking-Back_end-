
import json


FILE_NAME = "Acc_info.json"
INITIAL_DEPOSITS = "1000"
class Account(object):
    def __init__(self,holder,account_number):
        self.__holder = holder
        self.__account_number = account_number
        self.info = [self.__holder,self.__account_number]

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

    
    def deposit(self,amount):
        """This method first takes in the already saved data
            and checks if the holder already has an account and then 
            add the amount to be deposited into the old amount
            or if the holder is new creates new amount and adds it 
            it the initial deposit.
        """
        data = self.__load()
        
        if self.__holder in data:
            current_amount = int(data[self.__holder][1])+amount
            data[self.__holder] = [self.__account_number,current_amount]
            self.__save(data)
        else:
            current_amount= amount + int(INITIAL_DEPOSITS)
            data[self.__holder] = [self.__account_number,current_amount]
            self.__save(data)

    def withdraw(self,amount):
        """This method withdraws some amount from the holder's account if valid
        """
        data = self.__load()
        current_balance  = data[self.__holder][1]
        if amount >current_balance:
            print("Sorry Insufficient amount!")
        else:
            new_amount = current_balance -amount
            data[self.__holder] = [self.__account_number,new_amount]
            self.__save(data)
            print("Amount withdrawn sucessfully!")
            print("Thank you for Banking with us!")


    def check_balance(self):
        """The method feteches the current amount in the 
            holder's account
        """
        data = self.__load()
        if self.__holder in data:
            print("The amount in your account is","${:,}".format(data[self.__holder][1]))

    

