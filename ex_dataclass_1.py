from dataclasses import dataclass,Field

@dataclass
class Employee:
    name: str
    age: int
    gender: str


if __name__ == '__main__':
    e1 = Employee('Sasi',30,'M')
    e2 = Employee('Ramu',35,'M')

    print(e1.__dataclass_fields__)
    my_field = Field('city',str)
    print(my_field)