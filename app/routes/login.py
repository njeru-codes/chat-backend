from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from .. import  model , utils , auth
from ..database import get_db
from sqlalchemy.orm import Session

router = APIRouter()




@router.post('/login')
async def login(db: Session=Depends(get_db), user: OAuth2PasswordRequestForm = Depends()):
    user_db = db.query( model.User).filter( model.User.email== user.username).first()
    if not user_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"{user.username} email does not exists")
    if not utils.verify_password(user.password, user_db.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='wrong password')

    access_token = auth.create_access_token( data={"user_id": user_db.id})
    return { "access_token": access_token, "token_type": "bearer" , "user_id": user_db.id}
