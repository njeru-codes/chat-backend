import pusher
from dotenv import load_dotenv
import os

load_dotenv()


pusher_client = pusher.Pusher(
  app_id= os.environ.get('APP_ID'),
  key=os.environ.get('APP_KEY'),
  secret=os.environ.get('APP_SECRET'),
  cluster='mt1',
  ssl=True
)

def send_message(chat_id:str, sender:str, receiver:str, message:str):
    pusher_client.trigger(chat_id, 'event', {'message': message, 'receiver': receiver, "sender": sender})