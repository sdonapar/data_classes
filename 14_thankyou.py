from dataclasses import dataclass, field, InitVar, asdict, astuple, replace, is_dataclass
from typing import ClassVar
from datetime import datetime,timedelta

@dataclass
class PyConSession:
    name:str
    venue:str
    start_time: datetime
    presenter:str
    end_time: datetime = field(default=None)
    duration: InitVar[int] = 30
    thankyou_message: ClassVar[str] = "Thank you for listening"
    expect_question: ClassVar[str] = "Any Questions ?"

    def __post_init__(self,duration):
        self.end_time = self.start_time + timedelta(duration/(60*24)) # duration converted to days

if __name__ == '__main__':
    dataclasses_session = PyConSession(
        name = "What you need to know about data classes in Python 3.7",
        venue = "Hall 1",
        start_time = datetime(2018,10,7,12,30),
        presenter = "Sasidhar"
    )
    next_session = PyConSession(
        name = " Building better Python microservices using GRPC",
        venue = "Hall 1",
        start_time = datetime(2018,10,7,14,0),
        presenter = "Narendran R",
        duration=60
    )
    print("="*50)
    print(dataclasses_session)
    print(dataclasses_session.thankyou_message)
    print(dataclasses_session.expect_question)
    print("="*50)
    print(next_session)