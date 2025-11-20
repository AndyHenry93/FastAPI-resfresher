from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import field_validator


class UserBody(BaseModel):
    name: str
    age: int
    email: EmailStr

    @field_validator("age")
    def validate_age(cls, value):
        if value < 21:
            raise ValueError("age must be 21 and above")
        return value


class UserResponse(UserBody):
    id: str
    name: str
    age: int
    email: str
