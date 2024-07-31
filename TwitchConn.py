import os
import time
import random

from Handlers.ChatHandler import ChatThread
from Handlers.ElevenLabs import SpeachHandler
import Prompts
from filters import checkOffensiveness
import Secrets

from twitchio.ext import pubsub
import twitchio

#Sets up the connection to the Twitch channel
bot = twitchio.Client(token=Secrets.access_token)
bot.pubsub = pubsub.PubSubPool(bot)

roles = {
    #Put The Prompts In Here So You Can Select Them When Running The Code
    #Example | "name": Prompts.name
    }

#Defines the FFMPEG install or something I don't know I think it's broke
os.environ['PATH'] += os.pathsep + './ffmpeg/bin'
os.system('cls')

@bot.event()
async def event_pubsub_channel_points(event: pubsub.PubSubChannelPointsMessage): #The event for the channel point redeems
    #Gets the ID of the channel point redeem
    id = str(event.reward.id)
    
    #Used To Find The ID Of The Channel Point Redeem You Want To Trigger The AI 
    print(id) 
    if id != Secrets.channel_points_id: return
        
    #checks to see if the message (msg) given is offensive or not based on predetermined filters
    msg = event.input
    if len(msg) > 140: return
    if checkOffensiveness(msg): return
    
    response = ActiveThread.chat_with_history(msg)
    
    VoiceThread.GetVoiceAndPlay(msg)
    VoiceThread.GetVoiceAndPlay(response)
    print("~~~~~~~~~~~~~~~~~~~~~~~~")

async def main(): #main loop
    #Subscribes the Twitch bot to the specified PubSub Events
    topics = [
        pubsub.channel_points(str(Secrets.access_token))[int(Secrets.channel_id)]
    ]
    await bot.pubsub.subscribe_topics(topics)
    print("Starting Bot")
    await bot.start()
    
if __name__ == "__main__": #Starts the main loop of the code
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
            ActiveThread = ChatThread(role=active_role, gpt_model="gpt-4")
            break
        except Exception as e:
            os.system('cls')
            print("Sometihng went wrong with getting the character\n\n\n\n")
                
    #loads the Voice Handler and Mic Handler
    print(f"Step 2 | Loading {role.capitalize()}'s Voice")
    VoiceThread = SpeachHandler(voice_name=role, model="eleven_multilingual_v1")
    
    bot.loop.run_until_complete(main()) 