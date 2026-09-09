from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class UserRoleCreate(BaseModel):
    role_id: int = Field(gt=0)


class UserRoleResponse(BaseModel):
    user_id: int
    role_id: int
    assigned_at: datetime
    assigned_by: int

    model_config = ConfigDict(
        from_attributes=True,
    )