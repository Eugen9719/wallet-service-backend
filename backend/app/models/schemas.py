from typing import List
from uuid import UUID

from pydantic import BaseModel, Field, computed_field

from backend.app.models.user import UserBase


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class Msg(BaseModel):
    msg: str


class TokenPayload(BaseModel):
    sub: str


class WebhookRequest(BaseModel):
    transaction_id: str
    account_id: int
    user_id: int
    amount: int
    signature: str


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    email: str | None = Field(None, max_length=255)
    first_name: str | None = None
    last_name: str | None = None
    is_superuser: bool | None = None
    password: str | None = None  # Новый пароль (опционально)


class UserRead(UserBase):
    id: int

    @computed_field
    @property
    def full_name(self) -> str:
        return f"{self.first_name or ''} {self.last_name or ''}".strip()


class AccountCreate(BaseModel):
    pass


class AccountUpdate(BaseModel):
    pass


class PaymentCreate(BaseModel):
    transaction_id: str
    amount: int
    account_id: int


class PaymentUpdate(BaseModel):
    pass


class AccountRead(BaseModel):
    id: int
    account_number: str
    balance: float


class PaymentRead(BaseModel):
    id: UUID
    transaction_id: str
    amount: float


class AccountReadWithPayments(AccountRead):
    payments: List[PaymentRead]


class UserAccountRead(UserRead):
    accounts: List[AccountRead]
