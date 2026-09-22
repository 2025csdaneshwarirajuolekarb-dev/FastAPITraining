from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI() 
@app.get("/")
def home():
    return {"page": "Home"}
# to get this about page, you can go to http:// and put another /about at the end of the url and write about
   
@app.get("/about") 
def about():
    return {"page": "About","author":"Daneshwari"}

@app.get("/health")
def health():
    return {"status": "ok"}
#POST request
@app.post("/create")
def create_something():
    return {"item": "created" }
#path parameters
@app.get("/student/{usn}")
def get_result(usn):
    return {"usn": usn,"Result":"Distinction"}

#path parameters with type hint
@app.get("/candidate/{rollno}")
def get_candidate(rollno: int):
    return {"rollno": rollno,"Result":"Distinction","type":str(type(rollno))}

#pydantic model
class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True

@app.post("/items")
def create_item(item:Item):
    return {"received":item, "total_price":item.price*1.18}

