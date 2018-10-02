from dataclasses import dataclass

# no comparision methods

@dataclass
class Person:
    person_id: int
    name: str
    gender: str

if __name__ == '__main__':
    person_d1 = Person(100,'Guido','M')
    person_d2 = Person(200,'Eric V Smith','M')
    person_d3 = Person(100,'Guido','M')

    print(person_d1 == person_d3)