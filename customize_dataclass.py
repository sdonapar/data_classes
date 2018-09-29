from dataclasses import dataclass, field, fields

# init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False
@dataclass(unsafe_hash=True,order=True,frozen=False)
class Person:
    #default=,default_factory=,init=True,repr=True,hash=None,compare=True,metadata={}
    person_id: int = field(hash=True,compare=False,metadata={'description':'PersonId should be unique'})
    name: str = field(compare=True,hash=False)
    gender: str = field(repr=False,hash=False,compare=False)
    skills: list = field(repr=False,hash=False,compare=False,default_factory=list)
    

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