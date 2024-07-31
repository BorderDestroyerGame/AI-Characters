import openai
import tiktoken
import Secrets

#Looks At The String Given And Determines How Many Tokens It Would Take Up (OpenAI's Way Of Determining Length Of Text)
def num_tokens_from_string(string: str, encoding_name: str = "cl100k_base") -> int:
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

#Submits The New Prompt And Chat History To 
def GetResponse(prompt, model, temperature) -> str:
    completion = openai.ChatCompletion.create(
            model=model,
            messages=prompt,
            temperature=temperature
            )
    response = completion.choices[0].message.content
    return response

class ChatThread:
    def __init__(self, role, history:list=[], gpt_model="gpt-4o-mini", temperature=1.2, max_tokens=12000):
        openai.api_key = Secrets.openai_key
        
        self.chat_history = []
        try:
            self.chat_history.append({"role": "system", "content": role})
            if history != []:
                self.chat_history.append(history)
            
            self.gpt_model = gpt_model
            self.temperature = temperature
            self.max_tokens = max_tokens
        except Exception as e:
            print(e)
            exit()
    
    def chat_without_history(self, prompt=''):
        if not prompt:
            print("No input received!")
            return

        to_prompt = [{"role": "user", "content": prompt}]
        
        response = GetResponse(prompt=to_prompt, model=self.gpt_model, temperature=self.temperature)
        return response
        
    def chat_with_history(self, prompt=''):
        if prompt == '' or prompt == None:
            print("No input received!")
            return
        
        #adds the current prompt to the old messages
        self.chat_history.append({"role": "user", "content": prompt}) 
        
        #removes prompts based on max tokens
        history_tokens = num_tokens_from_string("\n".join(str(self.chat_history)))
        print(f"Chat History Token Length | {history_tokens}")
        while history_tokens > self.max_tokens:
            toPop = self.chat_history[1]
            self.chat_history.pop(1)
            print(f"Popped | /n{toPop}")
            history_tokens = num_tokens_from_string("\n".join(str(self.chat_history)))
            
        print(f"\nAsking A Question!\nCurrent History | ")
        for line in self.chat_history:
            print(f"{line}\n")
        
        
        response = GetResponse(prompt=self.chat_history, model=self.gpt_model, temperature=self.temperature)
        self.chat_history.append({"role": "system", "content": response})
        return response