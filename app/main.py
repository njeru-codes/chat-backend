from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import login , register , chats, message
from . import model
from .database import engine
import uvicorn


#creates tables/models in the database
model.Base.metadata.create_all(bind=engine)

app = FastAPI()

#CORS
origins = [
    "https://heroku.app.com",   #TODO insert frontend domains
    "http://localhost:3000",
    "https://supertalks.me",
    "https://supertalks"
    '[*]',
    "https://3000-njerucodes-frontendchap-4kq9qoh0e12.ws-eu87.gitpod.io"
    ]    

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)





app.include_router(login.router)
app.include_router(register.router)
app.include_router(chats.router)
app.include_router(message.router)




if __name__ == "__main__":
  uvicorn.run("server.api:app", host="0.0.0.0", port=5000)
