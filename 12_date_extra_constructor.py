from dataclasses import dataclass
from time import localtime

# example with alternate constructor

@dataclass
class Date:
    year: int
    month: int
    day: int

    @classmethod
    def today(cls):
        # this will not call the __init__ method
        d = cls.__new__(cls)
        t = localtime()
        d.year = t.tm_year
        d.month = t.tm_mon
        d.day = t.tm_mday
        return d

if __name__ == '__main__':
    d1 = Date(2018,9,29)
    d2 = Date.today()
    print(d1)
    print(d2)
