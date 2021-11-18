from gtts import gTTS
from playsound import playsound
audio="speech.mp3"
language='en'
sp=gTTS(text="Good Morning Friends, Welcome to My Git",lang=language,slow=False)
sp.save(audio)
playsound(audio)
print("=========Audio is Playing")
