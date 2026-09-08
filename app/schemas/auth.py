from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class LoginResponse(BaseModel):
    message: str
    user_id: int
    email: EmailStr
    full_name: str
    last_login_at: datetime

    model_config = ConfigDict(
        from_attributes=True,
    )