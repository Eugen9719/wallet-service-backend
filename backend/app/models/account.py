from decimal import Decimal
from typing import Optional, List

from sqlalchemy import Column, Numeric
from sqlmodel import SQLModel, Field, Relationship
from uuid import uuid4, UUID


class Account(SQLModel, table=True):
    __tablename__ = 'account'
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    name: str = Field(default=None, nullable=False)
    user_id: int = Field(foreign_key="user.id", description="ID связанного пользователя")
    balance: Decimal = Field(..., gt=0, description="Баланс",
                             sa_column=Column(Numeric(precision=10, scale=2)))

    # Связь многие-к-одному с User
    user: "User" = Relationship(back_populates="accounts")
    # Связь один-ко-многим с Payment
    payments: List["Payment"] = Relationship(back_populates="account")


# Класс платежа
class Payment(SQLModel, table=True):
    __tablename__ = 'payment'
    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
    account_id: int = Field(foreign_key="account.id")

    # Связь многие-к-одному с Account
    account: Account = Relationship(back_populates="payments")
