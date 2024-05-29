from gtts import gTTS
from datetime import datetime

from os import path, mkdir


temp_dir = "./temp"

if not path.isdir(temp_dir):
    mkdir(temp_dir)


def get_filename():
    """ Use Current Time (use even miliseconds) as filename """
    filename = datetime.now().strftime("%Y%m%d%H%M%S%f")
    return f"{temp_dir}/{filename}.mp3"


def text_to_speech(text: str, language: str = 'ko') -> str:
    speech = gTTS(text=text, lang=language, slow=False)
    print("----------------")
    print(speech)
    print("----------------")

    filename = get_filename()
    speech.save(filename)

    return filename
