from typing import Union, Annotated

from fastapi import APIRouter, Cookie, Depends
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.encoders import jsonable_encoder

from config.database import db
from models.user_model import *

router = APIRouter()

@router.get("/me",tags=["Users"])
def get_user():
    jwt_token = Cookie("jwt_auth")

    if jwt_token is None:
        return {"result":"No cookie found"}
    
    return {"result":"success"}

@router.post("/register",tags=["User","register"])
def register_user(user: RegisterUserModel):
    user_collection = db["users"]
    result = user_collection.insert_one(jsonable_encoder(user))
    if result is None:
        return {"result":"There is some internal error"}
    
    response = JSONResponse({"result":"success"})
    response.set_cookie(key = "jwt_token",value = "fake-key")
    return response

@router.post("/login",tags=["User","register"])
async def register_user(user: LoginUserModel):
    user_collection = db["users"]
    user = jsonable_encoder(user)
    result = user_collection.find_one({"email":user["email"],"password":user["password"]})
    if result is None:
        return {"result":"invalid login credentials"}
    
    response = JSONResponse({"result":"success"})
    response.set_cookie(key = "jwt_token",value = "fake-key")
    return response

@router.post("/logout",tags=["User","logout"])
def logout(jwt_token:str = Cookie(None)):
    if jwt_token is None:
        return {"result":"Error in request"}
    
    response = JSONResponse({"result":"success"})
    response.delete_cookie("jwt_auth")
    return response