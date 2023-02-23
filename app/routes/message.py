from fastapi import APIRouter, Depends
from ..auth import get_current_user


router = APIRouter()



@router.post('/message')
async def create_msg(user_id:int =Depends(get_current_user)):
    return

@router.delete('message/{message_id}')
async def delete_msg(message_id, user_id:int =Depends(get_current_user)):
    return