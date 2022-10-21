# Python Code: Review Classes' Concepts
class Holding:
    """Description of the class ."""
    # You have to stick the same style. 

    def __init__(self, name, date, nshares, price):
        self._name = name 
        self._date = date 
        self._nshares = nshares 
        self._price = price 
        
    def __repr__(self):
        return f"<{self._name} {self._date} {self._nshares} {self._price}>"


    def __str__(self):
        return (f"The shares' names {self._name} " +
                    f"The date: {self._date} "+
                    f"The number of shares is: {self._nshares} "+
                    f"The price of each share is: {self._price}")
    
