from fastapi import FastAPI, Depends
from typing import Optional
from . import schemas, models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session


app = FastAPI()

models.Base.metadata.create_all(bind = engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/") #defining the path operation decorator
async def root(): #defining a path operation function
    return {"data": "You are seeing the root directory"}

'''
remember : always put default path parameter decorator before 
dynamic path parameter decorator otherwise fastapi will read the 
dynamic path parameter first and it will not reach default path parameter decorator
'''

@app.get("/blog/{id}")
async def about(id):
    return {"data" : {"blog" : id}}

'''
Also when writing query parameters default valued parameter cannot be first
i.e. non default value query parameters cannot follow default parameter
eg. async def(limit : int = 10, published : bool) -> this will lead to error
'''

@app.post("/blog")
async def create_blog(blog: schemas.Blog, db : Session = Depends(get_db)):
    new_blog = models.Blog(title = blog.title, body = blog.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get("/blog")
async def get_all_blogs(db : Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

