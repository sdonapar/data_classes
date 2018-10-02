from dataclasses import dataclass

# 2 - make the class as immutable by setting frozen=True
@dataclass(order=True,frozen=True)
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

    persons = [person_d1,person_d2,person_d3]
    person_dict = {}
    person_dict[person_d1] = "person1"
    person_dict[person_d2] = "person2"
    person_dict[person_d3] = "person3"