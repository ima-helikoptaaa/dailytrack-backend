from motor.core import AgnosticDatabase

from app.core.security import get_password_hash
from app.crud.base import CRUDBase
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate

# ODM, Schema, Schema
class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    async def get_by_email(self, db: AgnosticDatabase, *, email: str) -> User | None: # noqa
        return await self.engine.find_one(User, User.email == email)
    
    async def create(self, db: AgnosticDatabase, *, obj_in: UserCreate) -> User: # noqa
        # TODO: Figure out what happens when you have a unique key like 'email'
        user = {
            **obj_in.model_dump(),
            "email": obj_in.email,
            "hashed_password": get_password_hash(obj_in.password) if obj_in.password is not None else None, # noqa
            "full_name": obj_in.full_name,
        }

        return await self.engine.save(User(**user))

user = CRUDUser(User)