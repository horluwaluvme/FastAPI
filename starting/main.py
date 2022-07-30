from fastapi import FastAPI, HTTPException
from typing import Optional,List
from pydantic import BaseModel


class Todo(BaseModel):
    name: str
    due_date: str
    description: str 
    
app = FastAPI(title= "Todo API")

#Create, Read, Update , Delete

store_todo = []

@app.get('/')
async def home():
    return{"Hello": "World"}

@app.post('/today')
async def create_todo(todo:Todo):
    store_todo.append(todo)
    return todo
@app.get('/todo/', response_model=List[Todo])
async def get_all_todos():
    return store_todo
    
@app.get('/todo/{id}')
async def get_todo(id: int):
    
    try:
        return store_todo[id]
    except:
        raise HTTPException(status_code=404, detail="Todo Not Found")
    
@app.put('/linux/{id}')
async def update_todo(id: int, todo: Todo):
    
    try:
        store_todo[id]= todo
        return store_todo[id]
    
    except:
        raise HTTPException(status_code=404, detail="Todo Not found")
    
    

#this is like a main model in Django

    
#class Package(BaseModel):
#    name: str
#    number: int
#    description: Optional[str] = None
    
#app = FastAPI()

#@app.get('/')
#async def hello_world():
#    return {"Hello": "World"}

#response module basically converts the 
#@app.post("/package/", response_model=Package, response_model_include={"description"})
#async def make_package( package: PackageIn):
#    return package


#for a query
#@app.post("/package/{priority}")
#async def make_package(priority: int, package: Package, value: bool):
#    return {"priority": priority, **package.dict(), "value": value}



 






#url
#@app.get("/component/{component_id}") #path parameter
#async def get_component(component_id: int):
#    return {"componet_id": component_id}


#@app.get("/component/") 
#async def read_component(number: int, text : Optional[str]):#query parameter
#    return {"number": number, "text": text}

