from pydantic import BaseModel
from typing import Optional

'''
When you want to send data from client to server you must send it as request body.
For that we need pydantic models.
When the server sends data to client it is called response body.
'''
class Blog(BaseModel):
    title : str
    body : str
    published : Optional[bool]