from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel


app = FastAPI()


students = {
    1: {
        "name": "femo",
        "age": "31",
        "class": "Graduate"
    }
     
}


class Student(BaseModel):
    name: str
    age: int
    year: str
    
class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None
    

#an end point is the same as Path in Api.

@app.get("/")
def index():
    return {"name": "first Data"}


@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(None, description="The ID of the student you want to view", gt=0, lt=5)):
    return students[student_id]


#http://127.0.0.1:8000/get-by-name?name=femo
@app.get("/get-by-name/{student_id}")
def get_student(*, student_id:int, name: Optional[str]= None, test : int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not found"}


@app.post("/create-student/{student_id}")
def create_student(student_id : int, student : Student):
    if student_id in students:
        return {"Error": "Student exists"}
    
    students[student_id] = student
    return students[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "Student does not exist"}

    if student.name != None:
        students[student_id].name = student.name
        
    if student.age != None:
        students[student_id].age = student.age
        
    if student.year != None:
        students[student_id].year = student.year
    
   
    return students[student_id]


@app.delete("/delete-studet/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error": "Student not presnt in db"}
    
    del students[student_id]
    return {"message has been deleted"}        


 

#End point parameter is used to return a data relating to an input in path or at teh endpoint.
#A query is used to pass a data/value inside a url
#The difference btw query and path parameter is initializing an onject both in the path and function







