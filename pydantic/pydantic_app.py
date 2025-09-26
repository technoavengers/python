from pydantic import BaseModel, Field
from enum import Enum
from typing import Annotated, Optional
from pydantic import validator
from fastapi import FastAPI
import uvicorn

app1 = FastAPI()

class Role(str, Enum):
    admin = "admin"
    user = "user"
    guest = "guest"

class User(BaseModel):
    id: int                # required
    name: Annotated[str, Field(min_length=3)]
    age: Annotated[int, Field(ge=12, le=60)]   
    country: str = "India" # default value
    role: Role             # required, must be one of the enum values

    @validator("name")
    def name_alpha(cls, v):
        if not v.isalpha():
            raise ValueError("Name must contain only alphabets")
        return v

    @validator("age")
    def check_age(cls, v, values):
        if v < 18 and values.get("country") == "USA":
            raise ValueError("Minors not allowed in USA records")
        return v

@app1.post("/users/")
async def create_user(user: User):
    return {"user": user}

# Run the application
if __name__ == "__main__":
    uvicorn.run(app1, host="127.0.0.1", port=8005)