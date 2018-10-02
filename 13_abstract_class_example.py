from abc import ABCMeta, abstractmethod
from dataclasses import dataclass

# abstract method example

class Employee(metaclass=ABCMeta):

    @abstractmethod
    def hire(self):
        pass

    @abstractmethod
    def fire(self):
        pass

@dataclass
class SoftwareEngineer(Employee):
    employee_id: int
    name: str

    def hire(self):
        print(f"Employee {self.name} is hired")

    def fire(self):
        print(f"Employee {self.name} is fired")

if __name__ == '__main__':
    s1 = SoftwareEngineer(100,"Ram")
    s2 = SoftwareEngineer(200,"Sam")

    print(s1)
    s1.hire()
    s2.fire()
