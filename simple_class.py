# Simple Class
class Person:

    def __init__(self,person_id: int,name: str,gender: str):
        self.person_id = person_id
        self.name = name
        self.gender = gender

    def __repr__(self):
        return f"Person(person_id={self.person_id},name={self.name})"

    def __hash__(self):
        return hash(self.person_id)
    
    def __eq__(self,other):
        return self.person_id == other.person_id
    
    def __ge__(self,other):
        return self.name.upper() >= other.name.upper()
    
    def ___le__(self,other):
        return self.name.upper() <= other.name.upper()
    
    def __gt__(self,other):
        return self.name.upper() > other.name.upper()

    def __lt__(self,other):
        return self.name.upper() < other.name.upper()

if __name__ == '__main__':
    person1 = Person(person_id=100,name='Guido',gender='M')
    person2 = Person(person_id=200,name='Eric V Smith',gender='M')
    person3 = Person(person_id=100,name='Guido',gender='M')

    print(person1 == person3)
    print(person1 >= person2)
    print(person2 >= person3)

