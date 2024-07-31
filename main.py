import os
import time

from Handlers.ChatHandler import ChatThread
from Handlers.ElevenLabs import SpeachHandler
import Handlers.MicHandler as vi
from Secrets import *
import Prompts

os.environ['PATH'] += os.pathsep + './ffmpeg/bin'
os.system('cls')

roles = {
    #Add The Prompts In Prompts.py Here
    "burgie": Prompts.burgie
}

if __name__ == "__main__":
    while True:
        #Gets a list of the available characters and lists them to the user
        choices = [item for item in dir(Prompts) if not item.startswith("__")]
        choices = ', '.join(choices)
        print(f"Available Characters | {choices}")

        #Loads the respective chat threads based on input role        
        try:
            role = str(input("Who would you like to talk to? | ")).lower()
            print(f"Step 1 | Loading {role.capitalize()}'s Model")
            active_role = roles[role]
            prompt = Prompts.base_prompt + active_role
            
            ActiveThread = ChatThread(role=prompt)
            break
        except Exception as e:
            os.system('cls')
            print("Sometihng went wrong with getting the character\n\n\n\n")
                
    #loads the Voice Handler and Mic Handler
    print(f"Step 2 | Loading {role.capitalize()}'s Voice")
    VoiceThread = SpeachHandler(voice_name=role, model="eleven_multilingual_v1")
    
    while True:
        use_mic = str(input("Would you like to use mic input? (Y/N) | ").lower())
        if use_mic == "y":
            use_mic = True
            break
        elif use_mic == "n":
            use_mic = False
            break
        else:
            print("Please answer with either 'Y' or 'N'!")
    
    if use_mic:
        print("Step 3 | Loading Mic Handler")
        MicHandler = vi.MicHandler()
    
    print("\n\n\n\n")
    
    while True:
        if use_mic:
            prompt = MicHandler.GetVoiceConst()
        else:
            prompt = str(input(f"What would you like to ask {role.capitalize()} | "))
        response = ActiveThread.chat_with_history(prompt)
        
        print(f"{role.capitalize()}'s Response | {response}")

        VoiceThread.GetVoiceAndPlay(response)