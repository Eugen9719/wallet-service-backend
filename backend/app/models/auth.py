from sqlmodel import SQLModel


class Token(SQLModel):
    access_token: str
    token_type: str = "bearer"


class Msg(SQLModel):
    msg: str


class TokenPayload(SQLModel):
    sub: str
