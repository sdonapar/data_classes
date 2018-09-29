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
        print(f"Employee {self.name} hired")

    def fire(self):
        print(f"Employee {self.name} fired")
