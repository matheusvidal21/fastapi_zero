from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from .database import get_session
from .models import User
from .security import get_current_user

T_Session = Annotated[Session, Depends(get_session)]
T_CurrentUser = Annotated[User, Depends(get_current_user)]
T_OAuth2Form = Annotated[OAuth2PasswordRequestForm, Depends()]
