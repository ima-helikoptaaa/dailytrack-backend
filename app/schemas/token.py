from pydantic import BaseModel, SecretStr
from odmantic import Model, ObjectId

class RefreshTokenBase(BaseModel):
    token: SecretStr
    authenticates: Model | None = None


class RefreshTokenCreate(RefreshTokenBase):
    authenticates: Model


class RefreshTokenUpdate(RefreshTokenBase):
    pass

class TokenPayload(BaseModel):
    sub: ObjectId | None = None
    refresh: bool | None = False

class Token(BaseModel):
    access_token: str
    refresh_token: str | None = None
