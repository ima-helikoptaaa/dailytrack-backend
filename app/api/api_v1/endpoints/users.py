from typing import Any

from fastapi import APIRouter, Body, Depends, HTTPException
from pydantic.networks import EmailStr
from motor.core import AgnosticDatabase

from app import crud, schemas
from app.api import deps

router = APIRouter()

@router.post("/", response_model=schemas.User)
async def create_user_profile(
    *,
    db: AgnosticDatabase = Depends(deps.get_db),
    password: str = Body(...),
    email: EmailStr = Body(...), 
    full_name: str = Body(""),
) -> Any:
    """
    Create new user without the need to be logged in.
    """
    user = await crud.user.get_by_email(db, email=email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="This username is not available.",
        )
    # Create user auth
    user_in = schemas.UserCreate(password=password, email=email, full_name=full_name)
    user = await crud.user.create(db, obj_in=user_in)
    return user