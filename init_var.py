from dataclasses import dataclass, field, InitVar
from typing import ClassVar

# init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False
@dataclass(unsafe_hash=True,order=True,frozen=False)
class Person:
    #default=,default_factory=,init=True,repr=True,hash=None,compare=True,metadata={}
    # class variable
    organization: ClassVar = "ABC Company"
    # other data members
    person_id: int = field(hash=True,compare=False,metadata={'description':'PersonId should be unique'})
    name: str = field(compare=True,hash=False)
    gender: str = field(repr=False,hash=False,compare=False)
    # init only variable
    salary_grade: InitVar[str] = field(default=None)
    skills: list = field(repr=False,hash=False,compare=False,default_factory=list)

    def __post_init__(self,salary_grade):
        if salary_grade=="A1":
            self.salary=15000
        elif salary_grade=="A2":
            self.salary=20000
        else:
            self.salary=5000

if __name__ == '__main__':
    person_d1 = Person(100,'Guido','M',designation='Sr Software Engineer')
    person_d2 = Person(200,'Eric V Smith','M',designation='Software Engineer')
    person_d3 = Person(100,'Guido','M')

    print(f"person_d1 == person_d3 -> {person_d1 == person_d3}")
    print(f"person_d1 >= person_2 -> {person_d1 >= person_d2}")
    print(f"person_d2 >= person_3 -> {person_d2 >= person_d3}")

    persons = [person_d1,person_d2,person_d3]
    person_dict = {}
    person_dict[person_d1] = "person1"
    person_dict[person_d2] = "person2"
    person_dict[person_d3] = "person3"