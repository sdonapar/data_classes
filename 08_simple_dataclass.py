from dataclasses import dataclass

# 3 - use unsafe_hash = True
#   - if your class is logically immutable but can nonetheless be mutated
#   - This is a specialized use case and should be considered carefully.
@dataclass(order=True,unsafe_hash=True)
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