from CreditCardClass import CreditCard
from RangeClass import Range

class PredatoryCreditCard(CreditCard):
    def __init__(self, customer, bank, account, limit, apr):
        super().__init__(customer, bank, account, limit)
        self._apr = apr
        self._chargetimes = 0
        self._minpayment = 0


    def charge(self, price):
        success = super().charge(price)
        self._chargetimes +=1
        if self._chargetimes > 10:
            self._balance +=1
        if not success:
            self._balance += 5
        return success

    def process_month(self):

        self._minpayment = max([0.01*self._balance, 35])

        if self._balance > 0:
            self._balance *= pow(1+self._apr/100, 1/12)

        print("Minimum payment is " + str(self._minpayment) + "$")

    def process_payment(self, payment):

        if self._minpayment > payment:
            print("APR is increased by 20% due to missing minimum payment")
            self._balance -=payment
            self._apr *= 1.2

        elif self._minpayment == payment:
            self._balance = 0

        else:
            self._balance -= payment
            print("You have negative balance")


if __name__ in '__main__':
    wallet = []
    wallet.append(PredatoryCreditCard('John Smith', 'Swiss Bank', '1234', 1000, 20.0))
    wallet.append(PredatoryCreditCard('Jack Smack', 'Greek Bank', '5678', 2000, 25.0))
    wallet.append(PredatoryCreditCard('Jimm Smock', 'Brick Bank', '9012', 3000, 18.0))

    wallet[0].charge(800)
    wallet[0].charge(300)
    wallet[1].charge(2*1000)
    wallet[2].charge(3*2000)

    for c in range(15):
        wallet[0].charge(10)
        balance = wallet[0].get_balance()
    print(balance)

    wallet[0].process_month()
    balance = wallet[0].get_balance()
    print(balance)

    wallet[0].process_payment(45)

    balance = wallet[0].get_balance()
    print(balance)


'''    for c in range(3):
        print( 'Customer = ', wallet[c].get_customer( ))
        print( 'Bank = ', wallet[c].get_bank())
        print( 'Account = ', wallet[c].get_account( ))
        print( 'Limit = ', wallet[c].get_limit( ))
        print( 'Balance = ', wallet[c].get_balance())
        #while wallet[c].get_balance( ) > 100:
        #    wallet[c].make_payment(100)
        #    print('New balance = ', wallet[c].get_balance())
        print()
'''


