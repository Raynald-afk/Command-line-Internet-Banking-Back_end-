import random
from collections import deque

def Account_pin_gen():
    """
    This function generates and returns a  pin and an 
    account number for the user.
    """
    # generating a pin
    pin_num = [str(n) for n  in range(10)]
    pin  = "".join(random.sample(pin_num,4))
    
    #generating account number
    part_1 = random.sample(random.randint(1,5),4)
    print(part_1)
    
    
def Account_info(first_name,second_name,Dob,addrees):
    info = deque()
    # storing the information into a deque
    full_name = first_name+" "+ second_name
    info.append(first_name)
    info.append(full_name)
    info.append(Dob)
    info.append(addrees)

    

# Account_info("Raynald","Osei","22/22/22","Patasi")
Account_pin_gen()