from typing import Any
from typing import Dict
from typing import List

from bson import ObjectId
from fastapi import FastAPI
from fastapi import HTTPException

from .database import user_collection
from .models import UserBody
from .models import UserResponse


app = FastAPI()


@app.get("/users")
def read_user() -> List[UserBody]:
    return list(user_collection.find())


@app.post("/user")
def create_user(user: UserBody) -> UserResponse:
    user_results = user_collection.insert_one(user.model_dump(exclude_none=True))
    return UserResponse(
        id=str(user_results.inserted_id), name=user.name, age=user.age, email=user.email
    )


@app.get("/user/{user_id}")
def get_user(user_id: str) -> UserResponse:
    # Validate ObjectId
    if not ObjectId.is_valid(user_id):
        raise HTTPException(status_code=400, detail="Invalid user ID format")

    # Query MongoDB
    db_user = user_collection.find_one({"_id": ObjectId(user_id)})

    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    # Convert MongoDB doc -> Pydantic
    return UserResponse(
        id=str(db_user["_id"]),
        name=db_user["name"],
        age=db_user["age"],
        email=db_user["email"],
    )


@app.delete("/user/{user_id}/")
def delete_user(user_id: str) -> Dict[str, Any]:
    if not ObjectId.is_valid(user_id):
        raise HTTPException(status_code=404, detail="Invalid Id!")
    user_collection.delete_one({"_id": ObjectId(user_id)})
    return {"msg": "User deletion successful!"}
