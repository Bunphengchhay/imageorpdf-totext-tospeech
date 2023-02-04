from gtts import gTTS
import os

def convert_textToSpeech(text, language):
    # Create a gTTS object
    tts = gTTS(text=text, lang=language) 
    # Save the generated speech to a file
    tts.save("speech.mp3") 
    # Play the generated speech on mac
    os.system("afplay speech.mp3")