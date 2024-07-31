from pydub import AudioSegment
import speech_recognition as sr
import whisper
import torch
import numpy as np
from number_parser import parse  
import keyboard

import pyaudio

class MicHandler:
    def __init__(self, pause_threshold:float = 1, whisper_model:str = "small.en"):
        #loads the recognizer to use for the mic
        r = sr.Recognizer()
        r.pause_threshold = pause_threshold
        self.r = r
        
        micIndex = 0
        self.mic = sr.Microphone(device_index=micIndex, sample_rate=16000)
        
        #UNCOMMENT THIS CODE TO FIND YOUR SPECIFIED MIC INDEX IF YOU DON'T KNOW IT
        #p = pyaudio.PyAudio()
        #for i in range(pyaudio.PyAudio.get_device_count(p)):
        #    print(pyaudio.PyAudio.get_device_info_by_index(p, i))
        
        #Adjusts The Microphone For Ambient Noise For Better Voice Recognition
        with self.mic as source:
            self.r.adjust_for_ambient_noise(source)
            
        #loads the whisper model specified to turn mic input to text
        model = whisper.load_model(whisper_model)
        self.model = model
    
    #Gets The Mic Input Every Time The Specified Key Is Pressed (In This Case F8)
    def GetVoicePress(self):
        print("Awaiting Input (f8)")
        keyboard.wait("f8")
        print("Awaiting Voice")
        
        with self.mic as source:        
            audio = self.r.listen(source)
            print('Done Listening')
            torch_audio = torch.from_numpy(np.frombuffer(audio.get_raw_data(), np.int16).flatten().astype(np.float32) / 32768.0)
            audio_data = torch_audio
            
            result = self.model.transcribe(audio_data,language='english',fp16=False)

            predicted_text = parse(result["text"])
            print("You said | " + predicted_text)
            return predicted_text
    
    #Gets The Mic Input Constantly Without Waiting For Input
    def GetVoiceConst(self):
        print("Awaiting Voice")
        
        with self.mic as source:        
            audio = self.r.listen(source)
            print('Done Listening')
            torch_audio = torch.from_numpy(np.frombuffer(audio.get_raw_data(), np.int16).flatten().astype(np.float32) / 32768.0)
            audio_data = torch_audio
            
            result = self.model.transcribe(audio_data,language='english',fp16=False)

            predicted_text = parse(result["text"])
            print("You said | " + predicted_text)
            return predicted_text