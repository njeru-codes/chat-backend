from fastapi import APIRouter, Depends, HTTPException, status
from .. import schemas
from ..database import get_db
from sqlalchemy.orm import Session
from .. import model, utils

router = APIRouter()


@router.post('/register', response_model=schemas.NewUserResponse)
async def register(user: schemas.User,  db: Session=Depends(get_db)):
    user_email = db.query( model.User).filter( model.User.email== user.email).first()
    if user_email != None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"{user.email} email already exists")

    user.password = utils.hash_function(user.password)
    new_user = model.User( **user.dict() )
    db.add( new_user)  #insert user into db
    db.commit()
    db.refresh(new_user)

    return {
        "email": new_user.email,
        "user_id": new_user.id
    }
