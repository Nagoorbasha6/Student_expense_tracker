from pydantic import BaseModel

class Student(BaseModel):
    id:int
    name:str
    pocket_money:float
    food:float
    travel:float
    other_expenses:float
    balance:float

