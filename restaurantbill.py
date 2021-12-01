import time
from datetime import date

today = date.today()

numofpeople_int = 0
billnum_float = 0

def work_out_bill():
    priceEach = float(billnum_float) / int(numofpeople_int)
    print("Each person will have to pay: " + str(priceEach))
    day = today.strftime("%d/%m/%Y")
    log = "(" + day + ") " + str(numofpeople_int) + " people had to pay a total price of " + str(billnum_float) + " and paid " + str(priceEach) + " each."
    with open('restaurant.log', 'a') as f:
        f.writelines("\n" + log)
    input("\nPress ENTER to go back to the begining.")
    start()
    
    

def input_people_number():
    numofpeople = input("How many people are there?: ")
    check_is_int_people(numofpeople)

def enter_bill_number():
    billnum = input("How much was the bill?: ")
    check_is_float_bill(billnum)
    
def check_is_int_people(numofpeople):
    try:
        val = int(numofpeople)
        global numofpeople_int
        numofpeople_int = numofpeople
        enter_bill_number()
    except ValueError:
        print("That is not a number.")
        input_people_number()

def check_is_float_bill(billnum):
    try:
        val = float(billnum)
        global billnum_float
        billnum_float = billnum
        work_out_bill()
    except ValueError:
        print("That is not a number.")
        input_people_number()

def start():
    print("Welcome to the meal price splitter!")
    input_people_number()

start()
