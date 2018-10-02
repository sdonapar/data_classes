
from typing import NamedTuple

# added in 3.5.2
# added support for variable annotation syntax in 3.6
# added support for default values, methods and docstings in 3.6.1

class Person(NamedTuple):
    person_id:int
    name:str
    gender:str = None

if __name__ == '__main__':
    person_n2 = Person(100,'Guido','M')

    print(person_n2) # nice __repr__ method
    print(person_n2.name) # access by name
    person_id,name,gender = person_n2 #unpack
    print(person_id,name,gender)
