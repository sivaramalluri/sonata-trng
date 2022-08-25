from exception import Account

def withdraw(balance,amount):
    if(balance<amount):
        raise  "not sufficient balance"
    #balance=balance-amount