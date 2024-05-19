# fastapi server example
from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn

from .chat import ChatRoom
from .tts import text_to_speech


app = FastAPI()
chat = ChatRoom()


@app.get("/")
def hello_world():
    """ API Test endpoint """
    return {"Hello": "World"}


@app.get("/tts/{lang}/{text}")
def get_tts_audio(lang: str, text: str) -> FileResponse:
    """ Get TTS audio from text
    :returns: FileResponse
    """
    filename = text_to_speech(text, lang)
    return FileResponse(filename, media_type="audio/mpeg")


@app.get("/chat/{to}/{message}")
def send_message(to: str, message: str):
    """ Send Chat Message to User
    !WARNING! DO NOT USE THIS FUNCTION IN PRODUCTION
    !WARNING! FOR DEMO PURPOSE ONLY
    :returns: Chat Room WebSocket
    """

    chat.send_message(to, message)
    return {"status": "success"}


@app.get("/chat/{user}")
def recv_message(user: str):
    """ Receive Chat Message from Server
    !WARNING! DO NOT USE THIS FUNCTION IN PRODUCTION
    !WARNING! FOR DEMO PURPOSE ONLY
    :returns: Chat Room WebSocket
    """

    return chat.recv_message(user)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)
