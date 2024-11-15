from dataclasses import dataclass


@dataclass
class Stock:
    """ "Represents a holding

    >>> s = Stock("GOOG", 100, 490.10)
    >>> s.name
    'GOOG'
    >>> s.shares
    100
    >>> s.price
    490.1
    >>> s.cost()
    49010.0
    >>> print('%10s %10d %10.2f' % (s.name, s.shares, s.price))
          GOOG        100     490.10
    >>> t = Stock("IBM", 50, 91.5)
    >>> t.name
    'IBM'
    >>> t.cost()
    4575.0
    >>> t.something()
    Traceback (most recent call last):
    ...
    AttributeError: 'Stock' object has no attribute 'something'
    """

    name: str
    shares: int
    price: float

    def cost(self):
        return self.shares * self.price
