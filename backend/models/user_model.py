from pydantic import BaseModel

class UserModel(BaseModel):
    name: str
    email: str
    password: str

class RegisterUserModel(BaseModel):
    name: str
    email: str
    password: str

class LoginUserModel(BaseModel):
    email: str
    password: str