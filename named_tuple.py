from typing import NamedTuple

class Person(NamedTuple):
    person_id: int
    name: str
    gender: str

if __name__ == '__main__':
    person_1 = Person(100,'Guido','M')
    person_2 = Person(200,'Eric V Smith','M')
    person_3 = Person(100,'Guido','M')

    print(person_1 == person_3)
    print(person_1 >= person_2)
    print(person_2 >= person_3)