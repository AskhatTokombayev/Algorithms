from RangeClass import Range

class CreditCard:
    def __init__(self, customer, bank, account, limit):
        self._customer = customer
        self._bank = bank
        self._account = account
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        return self._customer


    def get_bank(self):
        return self._bank

    def get_account(self):
        return self._account

    def get_limit(self):
        return self._limit

    def get_balance(self):
        return self._balance

    def charge(self, price):
        if self._balance + price < self._limit:
            self._balance += price
            return True
        else:
            return False

    def make_payment(self,amount):
        self._balance-=amount
        return self._balance


if __name__ in '__main__':
    wallet = []
    wallet.append(CreditCard('John Smith', 'Swiss Bank', '1234', 1000))
    wallet.append(CreditCard('Jack Smack', 'Greek Bank', '5678', 2000))
    wallet.append(CreditCard('Jimm Smock', 'Brick Bank', '9012', 3000))

    for val in Range(1,17):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)


    for c in range(3):
        print( 'Customer = ', wallet[c].get_customer( ))
        print( 'Bank = ', wallet[c].get_bank())
        print( 'Account = ', wallet[c].get_account( ))
        print( 'Limit = ', wallet[c].get_limit( ))
        print( 'Balance = ', wallet[c].get_balance())
        while wallet[c].get_balance( ) > 100:
            wallet[c].make_payment(100)
            print('New balance = ', wallet[c].get_balance())
        print()