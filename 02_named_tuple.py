
from collections import namedtuple

# added in Python 2.6
# immutable

Person = namedtuple('Person',['person_id','name','gender'])

if __name__ == '__main__':
    person_n1 = Person(100,'Guido','M')

    print(person_n1) # nice __repr__ method
    print(person_n1.name) # access by name
    person_id,name,gender = person_n1 #unpack
    print(person_id,name,gender)