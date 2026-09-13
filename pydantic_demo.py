## pydantic is a data validation and data parsing library for python It ensure that the data you work with 
## is a correct structured and type safe

from pydantic import BaseModel, EmailStr, Field
from typing import Optional



class Student(BaseModel):
    
    name:str='asad'
    age:Optional[int]=None
    email:EmailStr
    cgpa:float=Field(gt=0,lt=10)

new_student={'name':'asad','age':'32','email':'asadlagdebw@gmail.com','cgpa':'9'}

Student=Student(**new_student)
print(Student)
