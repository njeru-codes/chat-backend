from fastapi import APIRouter, Depends, HTTPException, status
from ..auth import get_current_user
from .. import schemas, model , pusher
from ..database import get_db
from sqlalchemy.orm import Session


router = APIRouter()



@router.post('/message')
async def create_msg(message: schemas.NewMessage, user_id:int =Depends(get_current_user), db: Session=Depends(get_db)):
    user = db.query(model.User).filter( model.User.id == user_id ).first()
    user_email = user.email

    chat = db.query(model.Chat).filter( model.Chat.id == message.chat_id ).first()
    authorized = False
    for email in chat.users:
        if email == user_email:
            authorized = True
    if not authorized:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="you cant send message to chat")
    new_message = model.Message( **message.dict() )
    db.add( new_message)  #insert user into db
    db.commit()
    db.refresh(new_message)

    pusher.send_message(str(message.chat_id), message.sender , message.receiver, message.message)
    
    
    return new_message

@router.delete('message/{message_id}')
async def delete_msg(message_id:int, user_id:int =Depends(get_current_user) , db: Session=Depends(get_db)):
    message = db.query(model.Message).filter(model.Message.id == message_id).first()
    if record:
        db.delete(record)
        db.commit()
        return f"deleted message with id{ message_id}"
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"message with id{message_id} not found")