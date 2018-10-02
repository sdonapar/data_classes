

# PEP 484 - Type hints
# Python3.5
def greeting(name: str) -> str:
    return f"Hello {name}"


# PEP 526 - Syntax for variable annotations
# Python3.6

class Vehicle:
    make: str = 'Maruti'
    year_of_manufacture: int = 2018

    def __init__(self, registration_number: str ):
        self.registration_number = registration_number
    
    def __repr__(self):
        return f"Vehicle({self.registration_number})"

# PEP 557 - Dataclasses
# Python3.7

from dataclasses import dataclass

@dataclass
class Vehicle:
    registration_number: str
    make: str = 'Maruti'
    year_of_manufacture: int = 2018


# NamedTuple example

from typing import NamedTuple

class Employee(NamedTuple):
    name: str
    age: float
    gender: str

    
