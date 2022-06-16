# import FastAPI as an object
from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

# create an instance of the FastAPI object to be accessed later
app = FastAPI()

students = {
    1: {
        "first_name": "Rodgers",
        "last_name": "Nyangweso",
        "age": 28,
        "year": "year 4",
        "active": "true"
    },
    2: {
        "first_name": "Harvey",
        "last_name": "Nyangweso",
        "age": 1,
        "year": "year 0",
        "active": "true"
    },
    3: {
        "first_name": "Robert",
        "last_name": "Ochieng",
        "age": 25,
        "year": "year 2",
        "active": "true"
    },
    
    4: {
        "first_name": "Irene",
        "last_name": "Ochieng",
        "age": 27,
        "year": "year 3",
        "active": "true"
    },
    
    5: {
        "first_name": "Wilson",
        "last_name": "Nyangweso",
        "age": 65,
        "year": "",
        "active": "true"
    }
}

# creating a student class
class Student(BaseModel):
    first_name : str
    last_name : str
    age: int 
    year: str
    active : bool

# Update student class
class UpdateStudent(BaseModel):
    first_name : Optional[str] = None
    last_name : Optional[str] = None
    age : Optional[int] = None
    year : Optional[str] = None
    active : Optional[bool] = None

# Creating an endpoint
# create an endpoint which is one end of a communication channel.
@app.get("/")
def index():
    return {"first_name": "Rodgers"}

# Using Path parameter
@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(None, description = "The ID of the student you want to view", gt = 0, lt = 10)):
    return students[student_id]

# Using Query Parameter
@app.get("/get-by_first_name")
def get_student(*, first_name: Optional[str] = None): # an optional query parameter
    for student_id in students:
        if students[student_id]["first_name"] == first_name:
            return students[student_id]
        
    return {"Data": "Not Found"}

# Combining Path and Query parameter together
@app.get("/get-by_first_name/{student_id}")
def get_student(*, student_id: int, first_name: Optional[str] = None): # an optional query parameter
    for student_id in students:
        if students[student_id]["first_name"] == first_name:
            return students[student_id]
        
    return {"Data": "Not Found"}

# Request Body and POST method
@app.post("/create-student/{student_id}")
def create_student(student_id : int, student : Student):
    if student_id in students:
        return {"ERROR": "Student already exists"}
    
    students[student_id] = student
    return students[student_id]

# PUT Method - used to update already existing data
@app.put("/update-student/{student_id}")
def update_student(student_id : int, student : UpdateStudent):
    if student_id not in students:
        return {"ERROR": "Student already exists"}
        
    if student.first_name != None:
        students[students_id].first_name = student.first_name
        
    if student.last_name != None:
        students[student_id];last_name = student.last_name
        
    if student.age != None:
        students[student_id].age = student.age
        
    if student.year != None:
        students[student_id].year = student.year
        
    if student.active != None:
        students[student_id].active = student.active
        
# Delete Method
@app.delete("/delete-student/{student_id}")
def delete_student(student_id : int):
    if student_id != students:
        return {"ERROR": "Student does not exists"}
    
    del students[student_id]
    return {"Message" : "Student Deleted Successfully"}