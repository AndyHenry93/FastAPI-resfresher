from typing import Dict

from fastapi import Depends
from fastapi import FastAPI
from fastapi import HTTPException
from sqlalchemy.orm import Session

from .database import SessionLocal
from .database import User
from .database import UserBody
from .database import UserResponse


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/user/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)) -> UserBody:
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.post("/user")
def add_new_user(user: UserBody, db: Session = Depends(get_db)) -> UserResponse:
    new_user = User(name=user.name, email=user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.put("/user/{user_id}")
def update_user(
    user_id: int, user: UserBody, db: Session = Depends(get_db)
) -> UserResponse:
    db_user = db.query(User).get(user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_user.name = user.name
    db_user.email = user.email

    db.commit()
    db.refresh(db_user)
    return UserResponse(name=db_user.name, email=db_user.email, msg="Update successful")


@app.delete("/user/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)) -> Dict[str, str]:
    db_user = db.query(User).get(user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    return {"detail": "User_deleted"}
