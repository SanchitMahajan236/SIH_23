from fastapi import FastAPI
import os

# Importing the routes
from routes import user,training_online

app = FastAPI()

# Including each route
app.include_router(user.router,prefix="/user",tags=["User"])

app.include_router(training_online.router,prefix="/training/online",tags=["training_online"])

@app.get("/")
async def root():
    return {"message": "Hello World"}

