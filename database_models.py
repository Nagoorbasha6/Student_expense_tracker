from sqlalchemy import Column,Integer,Float,String
from database import Base

class Student(Base):
    __tablename__='student_expense_tracker'


    id=Column(Integer, primary_key=True)
    name=Column(String)
    pocket_money=Column(float)
    food=Column(float)
    travel=Column(float)
    other_expenses=Column(float)
    balance=Column(float)
