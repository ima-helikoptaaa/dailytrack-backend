from pydantic import BaseModel
from odmantic import ObjectId

class TokenPayload(BaseModel):
    sub: ObjectId | None = None
    refresh: bool | None = False
