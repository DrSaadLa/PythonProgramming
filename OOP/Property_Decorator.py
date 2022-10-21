# Python Code: Review Classes' Concepts
class Holding:
    """Description of the class ."""
    # You have to stick the same style.

    def __init__(self, name, date, shares, price):
        self._name = name
        self._date = date
        self._shares = shares
        self._price = price

    def __repr__(self):
        return f"<{self._name} {self._date} {self._shares} {self._price}>"


    def __str__(self):
        return (f"The shares' names {self._name}, " +
                    f"The date: {self._date}, "+
                    f"The number of shares is: {self._shares}, "+
                    f"The price of each share is: {self._price}")


    def sell_shares(self, nshares):
        self._shares = self._shares - nshares

    # Create a buy_shares method.
    def buy_shares(self, nshares):
        self._shares += nshares


    def total_return(self):
        return self._shares * self._price
from holding import Holding


h1 = Holding("IBM", "2020-1-10", 50, 47.3)

# print(h1.__dict__)
#
# # print(h1)
# print(repr(h1))

# Print the number of shares
# print(h1._shares)
#
# # Apply the sell method
# h1.sell_shares(20)
# print(h1._shares)
#
# # Apply the buy_method
# h1.buy_shares(65)

print(h1._shares)

print(h1.total_return())
