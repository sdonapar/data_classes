from dataclasses import dataclass, field, fields

# init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False
@dataclass(unsafe_hash=True,order=True,frozen=False)
class Person:
    #default=,default_factory=,init=True,repr=True,hash=None,compare=True,metadata={}
    person_id: int = field(hash=True,compare=False,metadata={'description':'PersonId should be unique'})
    name: str = field(compare=True,hash=False)
    gender: str = field(repr=False,hash=False,compare=False)
    designation: str = field(hash=False,compare=False)
    skills: list = field(repr=False,hash=False,compare=False,default_factory=list)

    def __post_init__(self):
        if self.designation=="Software Engineer":
            self.salary=15000
        elif self.designation=="Sr Software Engineer":
            self.salary=20000
        else:
            self.salary=5000

if __name__ == '__main__':
    person_d1 = Person(100,'Guido','M','Sr Software Engineer')
    person_d2 = Person(200,'Eric V Smith','M','Software Engineer')
    person_d3 = Person(100,'Guido','M','Director')

    print(f"person_d1 == person_d3 -> {person_d1 == person_d3}")
    print(f"person_d1 >= person_2 -> {person_d1 >= person_d2}")
    print(f"person_d2 >= person_3 -> {person_d2 >= person_d3}")

    persons = [person_d1,person_d2,person_d3]
    person_dict = {}
    person_dict[person_d1] = "person1"
    person_dict[person_d2] = "person2"
    person_dict[person_d3] = "person3"