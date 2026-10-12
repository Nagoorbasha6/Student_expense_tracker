from fastapi import FastAPI
from models import Student



app = FastAPI()
Students=[
    Student(id=1,name='Basha',pocket_money=5000,food=2000,travel=1000,other_expenses=500,balance=1500),
    Student(id=2,name='Prabash',pocket_money=6000,food=2500,travel=800,other_expenses=1000,balance=1700),
    Student(id=3,name='jagadeesh',pocket_money=4000,food=3000,travel=500,other_expenses=500,balance=0)

]

@app.get('/Students')
def get_students():
    return Students

@app.get('/Students/{id}')
def get_student_id(id:int):
    for i in range(len(Students)):
        if Students[i].id==id:
            return Students[i]
    return "invalid id"

@app.post("/Students")
def add_student(student:Student):
    Students.append(student)
    return student

@app.put("/Students/{id}")
def update_student(id:int,student:Student):
    for i in range(len(Students)):
        if Students[i].id==id:
            Students[i]=student
            return Students[i]
    return 'invalid id'

@app.delete("/Students")
def delete_student(id:int):
    for i in range (len(Students)):
        if Students[i].id==id:
            del Students[i]
            return 'deleted successfully'
        else:
            return 'invalid id'

