from playsound import playsound
from gtts import gTTS


audio = 'speech.mp3'
language = 'en'
sp = gTTS(text = "enter the text which you want to convert to audio file", lang = language,slow=False)
sp.save(audio)
playsound(audio)
