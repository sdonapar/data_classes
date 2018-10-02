from dataclasses import dataclass

# The dataclass decorator is typically used with no parameters and no parentheses. 
# However, it also supports the following kword parametes
# init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False

@dataclass(order=True)
class Person:
    person_id: int
    name: str
    gender: str

if __name__ == '__main__':
    person_d1 = Person(100,'Guido','M')
    person_d2 = Person(200,'Eric V Smith','M')
    person_d3 = Person(100,'Guido','M')

    print(person_d1 == person_d3)
    print(person_d1 >= person_d2)
    print(person_d2 >= person_d3)