from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List


class UserBase(SQLModel):
    email: str = Field(unique=True, index=True, max_length=255)
    first_name: Optional[str] = None
    last_name: Optional[str] = None


class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    is_superuser: bool = Field(default=False)
    hashed_password: str

    # Связь один-ко-многим с Account
    accounts: List["Account"] = Relationship(
        back_populates="user",
        sa_relationship_kwargs={"cascade": "all, delete-orphan"}
    )
