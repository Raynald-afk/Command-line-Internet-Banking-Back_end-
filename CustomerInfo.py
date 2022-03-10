import random
from collections import namedtuple


def Account_pin_gen():
    """
    This function generates and returns a  pin and an 
    account number for the user.
    """
    # generating a pin
    pin_num = [str(n) for n  in range(10)]
    pin  = "".join(random.sample(pin_num,4))
    
    #generating account number
    acc_num = ""
    for _ in range (3):
        sample = ""
        for _ in range (1):
            x_1 = random.randint(1,9)
            y_1 = "00"
            x_2  = random.randint(5,9)
        sample = str(x_1) +str(y_1)+str(x_2)
        acc_num += sample
    return acc_num , pin


    
    
def Account_info(first_name,second_name,Dob,address,contact_number):
        details = namedtuple("info","first_name second_name Dob address contact")
        info = details(first_name,second_name,Dob,address,contact_number)
        return info

