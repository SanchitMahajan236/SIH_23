from fastapi import APIRouter

router = APIRouter()

@router.get("/me",tags=["Users"])
def get_user():
    return {"result":"success"}