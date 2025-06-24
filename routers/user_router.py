from fastapi import APIRouter, HTTPException
from schemas.user import UserCreate, UserUpdate, UserOut
from services import user_service

router = APIRouter()

@router.post("/", status_code=201)
def create_user(user: UserCreate):
    user_service.create_user(user)
    return {"message": "User created"}

@router.get("/", response_model=list[UserOut])
def read_users():
    return user_service.get_all_users()

@router.put("/{user_id}")
def update_user(user_id: int, user: UserUpdate):
    user_service.update_user(user_id, user)
    return {"message": "User updated"}

@router.delete("/{user_id}")
def delete_user(user_id: int):
    user_service.delete_user(user_id)
    return {"message": "User deleted"}
