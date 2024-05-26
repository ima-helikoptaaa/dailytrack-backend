from typing import Generator

from fastapi import HTTPException, status
from jose import jwt
from pydantic import ValidationError

from app import schemas
from app.core.config import settings
from app.db.session import MongoDatabase

def get_db() -> Generator:
    try:
        db = MongoDatabase()
        yield db
    finally:
        pass

def get_token_payload(token: str) -> schemas.TokenPayload:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.JWT_ALGO])
        token_data = schemas.TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    return token_data