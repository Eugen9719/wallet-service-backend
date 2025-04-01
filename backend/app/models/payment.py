from uuid import UUID, uuid4

from sqlmodel import SQLModel, Field, Relationship


class Payment(SQLModel, table=True):
    __tablename__ = 'payment'
    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
    transaction_id: str
    amount:int
    account_id: int = Field(foreign_key="account.id")

    # Связь многие-к-одному с Account
    account: "Account" = Relationship(back_populates="payments")
