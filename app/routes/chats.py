from fastapi import APIRouter, Depends, HTTPException, status
from ..auth import get_current_user
from .. import schemas, model
from ..database import get_db
from sqlalchemy.orm import Session
from sqlalchemy import ARRAY





router = APIRouter()



@router.get('/chat')
async def get_chats(user_id:int =Depends(get_current_user), db: Session=Depends(get_db)):
    user = db.query(model.User).filter( model.User.id == user_id ).first()
    chats = db.query(model.Chat).filter( model.Chat.users.contains([user.email])  ).all()
    if chats == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='no chats were found')
    return chats

@router.post('/chat')
async def create_chat(chat: schemas.NewChat, user_id:int =Depends(get_current_user), db: Session=Depends(get_db)):
    chat_db = db.query(model.Chat).filter( model.Chat.users.contains( [ chat.user, chat.user2] ) ).first()
    if chat_db != None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"chat already exists {chat_db.id}")

    new_chat = model.Chat()
    new_chat.users= [ chat.user, chat.user2]
    db.add( new_chat)  #insert user into db
    db.commit()
    db.refresh(new_chat)

    return {
        "chat_id": new_chat.id,
        "users": new_chat.users
    }

@router.get('/chat/{chat_id}')
async def get_chat(chat_id: int, user_id:int =Depends(get_current_user), db: Session=Depends(get_db)):
    chat = db.query(model.Chat).filter( model.Chat.id == chat_id ).first()
    if not chat:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"chat with id {chat_id} not found")

    messages = db.query(model.Message).filter( model.Message.chat_id == chat.id).all()
    
    return messages