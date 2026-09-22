from fastapi import FastAPI

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