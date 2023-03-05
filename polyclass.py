import re
import random


"""
References
- https://github.com/infusion/Polynomial.js/blob/master/polynomial.js
- https://github.com/DmitryNakhimovich/Polynomial-class/blob/master/polynom.py
"""

class Polynomial:
    """ Represents polynomilas fomr manipulation"""
    def __init__(self, args) -> None:
        """" 
        Build a polynomial from a list of coefficients in 
        descending order or list of tuples in the form (coefficient, exponent)
        """ 
        print(type(args), type(args[0]), args)

    def from_string(self, expression: str):
        """ Builds polynomial class form string. """
        pass

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass
    
    def __truediv__(self, other):
        pass

    def format(self):
        pass

    def __repr__(self):
        # official representation
        pass

    def __str__(self):
      # informal
      pass
    
    def __call__(self, *args, **kwargs):
        pass



    
    def factor(self):
        pass

    @property
    def degree(self):
        return 0




x = Polynomial([1, 2, 3, 4, 5, 6])
y = Polynomial('x^2-5x+6')
#z = Polynomial(x)
a = Polynomial([(3, 6), (4, 5), (2, 3)])



