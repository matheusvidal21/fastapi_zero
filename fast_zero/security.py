from pwdlib import PasswordHash
from jwt import encode, decode
from jwt.exceptions import PyJWTError
from .settings import Settings
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from sqlalchemy import select
from .models import User
from .database import get_session

pwd_context = PasswordHash.recommended()

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data_claims: dict):
    to_encode = data_claims.copy()
    
    expire = datetime.now(tz=ZoneInfo('UTC')) + timedelta(Settings().ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({'exp': expire})
    encoded_jwt = encode(to_encode, Settings().SECRET_KEY, algorithm=Settings().ALGORITHM)
    return encoded_jwt

aouth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

def get_current_user(session: Session = Depends(get_session), token: str = Depends(aouth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Could not validate credentials',
        headers={'WWW-Authenticate': 'Bearer'},
    )
    
    try:
        payload = decode(token, Settings().SECRET_KEY, algorithms=[Settings().ALGORITHM])
        email: str = payload.get('sub')
        if not email:
            raise credentials_exception    
    except PyJWTError:
        raise credentials_exception
    
    
    user = session.scalar(
        select(User).where(User.email == email)
        )
    if not user:
        raise credentials_exception
    return user