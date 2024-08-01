# AICharacters
A simple app that allows you to converse and create AI personalities using OpenAI's API along with Elevenlabs. Written and developed by Nathaniel (BorderDestroyer) Davies.

Feel free to use the code and alter it however you want! If you do, credit would be nice and appreciated!

## Setup
1) Make sure that you have python 3.10.11 installed. You can go ahead and get the installation here (https://www.python.org/downloads/release/python-31011/)

2) Run `python -m pip install -r requirements.txt` in the project folder to install all packages needed.

3) You will need to set up an account with Elevenlabs and OpenAI in order to use the code. After doing so, you will then receive an API key from each of them, which you can then assign in the `Secrets.py` file.

4) In `Prompts.py` you can assign a variable to hold the information on how you want your AI to behave and respond. This is designed so you can create and save as many AI Personalities as you want, and load them after running the program.

5) Finally, you will want to assign the Elevenlabs voice to your prompt. In `main.py` in the `roles` dictionary, first put the voice used in elevenlabs as a string, and then a reference to the variable created in step 4 (example | "burgie": Prompts.burgie)

## Running The Application
1) Run 'main.py'
2) If you have the voice mode set to `MicHandler.GetVoiceConst()` (see line 61 in main.py) speak what you want to ask/tell the AI, and then wait for a response. It will automatically pick up as soon as you start talking, and end when it detects you have stopped. 
3) If you have the voice mode set to `MicHandler.GetVoicePress()` go ahead and press the key designated in `MicHandler.py line 37` (default is 'F8')
4) You can change if you want the AI to remember what you had said previously in the conversation, or if you want it to only remember what you had just said by changing `line 64 in main.py` between `ActiveThread.chat_with_history(prompt)` and `ActiveThread.chat_without_history(prompt)`
