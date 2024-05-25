from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["argon2", "bcrypt"], deprecated="auto"
)  # current defaults: $argon2id$v=19$m=65536,t=3,p=4, "bcrypt" is deprecated

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)
