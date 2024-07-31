import elevenlabs
import Secrets
import time

import keyboard

class SpeachHandler:
    def __init__(self, voice_name:str, model:str = "eleven_monolingual_v1"):
        self.voice_name = voice_name
        self.model = model
        self.api_key = Secrets.elevenlabs_key
        
        #Initializes The Elvenlabs API
        elevenlabs.set_api_key(Secrets.elevenlabs_key)
        voices = elevenlabs.Voices.from_api()
        
        #Attempts To Find The Selected Voice In Elevelabs, Erorrs Out If Not Found
        for voice in voices:
            voice = str(voice).split(" ")[1].split("'")[1]
            if voice == voice_name.capitalize():
                self.voice = voice
                break
    
    #Function To Convert The Response Of The AI Into MP3 And Play It Through The Default Speakers    
    def GetVoiceAndPlay(self, prompt = ""):
        if not prompt:
            print("Nothing was given to say!")
            return
        
        while True:
            try:
                audio = elevenlabs.generate(
                    text=prompt,
                    model=self.model,
                    voice=self.voice
                )
                elevenlabs.play(audio)
                break
            except elevenlabs.RateLimitError:
                print("There Was A Rate Limit Error With ElevenLabs!")
                time.sleep(2)
            except elevenlabs.APIError:
                print("There was a problem with the ElevenLabs API. Sleeping for 10 seconds")
                time.sleep(10)
                