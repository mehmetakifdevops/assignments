from gtts import gTTS
from playsound import playsound

def play_audio(path_of_audio):
    
    playsound(path_of_audio)
    
def convert_to_audio(text):
    my_audio = gTTS(text)
    my_audio.save("read.mp3")
    play_audio("read.mp3")
    
convert_to_audio("hello, my name is Tom and I'm 28 years old.")
