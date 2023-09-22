from fastapi import FastAPI

# Importing the routes
from routes import user

app = FastAPI()

# Including each route
app.include_router(user.router,prefix="/user",tags=["User"])

@app.get("/")
async def root():
    return {"message": "Hello World"}
