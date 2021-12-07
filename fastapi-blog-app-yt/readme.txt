python -m venv virenv - creating virtual environment

virenv\Scripts\activate.bat - activating virtual environment

python.exe -m pip install --upgrade pip - upgrade pip

pip install uvicorn - install uvicorn server

deactivate - deactivate virtual environment

pip install -r requirements.txt - download all requirements for the project

SQL ALCHEMY STEPS:
------------------
1. create engine
2. declare a base
3. create session
4. create models.py and import base
5. create table class and inherit the base
6. import models and schemas file into main app file
7. import engine from database into main app file
8. models.Base.metadata.create_all(bind = engine)
9. from sqlalchemy.orm import Session
10. import Depends from fastapi
11. declare the get_db function and pass it as a 
default value to the parameter of you post method
12. to declare get_db function first import SessionLocal from .database
13. inside get_db function write db = SessionLocal()
14. in try : yield db , in finally : db.close()
15. In post method path function create object of models.classname
and pass the schemas parameters to the models object, 
i.e. pass the request body to the database.
---------------------------------------------------------------------------------



