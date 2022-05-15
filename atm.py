from ast import If
from random import randint

def atm_nos(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def split_card_no(num):
    split = 4
    split_num = [num[i:i+split] for i in range(0,len(num),split)]
    print(split_num)


class atm(object):
    def __init__(self, Cardno, pin, cvv):
        self.Cardno = Cardno
        self.pin = pin
        self.cvv = cvv






def start():
    print("Hello, Thanks for opening your new account! Here's your new card")
    print(f""" 
    ______________________________________
   |                                      |
   |        card no:         {atm_nos(12)} |
   |--------------------------------------|
   |                                      |
   |         CVV:{atm_nos(3)}                      |
   | ✰ ✰ ✰                      COOL BANK |
   |______________________________________|
 
    """)

    response = input('Would you like to deposit some of your savings? [y/n]: ')
    if (response == 'y'):
        amount = input('Enter your amount to be deposited :')
        print(f'your money of Rs {amount} have been deposited')
        withdraw_q = input('would you like to withdraw some money? [y/n]:')
        if(withdraw_q == 'y'):
            money_to_be_withdrawn = input('How much?: ')
            def withdraw(amount_to_be_withdrawn):
                money = int(amount_to_be_withdrawn)
                deposit = int(amount)
                if (deposit<money):
                    print('Your balance is not sufficient for the required withdrawal !')
                elif(deposit>= money):
                    print("amount withdrawn. here's your money")
            withdraw(money_to_be_withdrawn)
    elif (response == 'n'):
        print('alright')
    else:
        print('We didnt get it.')

start()
