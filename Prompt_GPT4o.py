import openai
import Imp4
#import prompt
#import Coverage_prompt
from openai import AzureOpenAI

endpoint,key,api_v = Imp4.get_imp()

client = AzureOpenAI(
  azure_endpoint = endpoint, 
  api_key=key,  
  api_version= api_v
)

import base64
image_path = 'C:\Shilz\Shilz_Experiment\Shilz_Exp_2\Skjermbilde 2024-06-21 152626.png'

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

image_temp = encode_image(image_path) 

info = f"""You  test  a  system  whose  lifecycle  is  modeled  by  the  state  transition  diagram  shown  below.  The 
system starts in the INIT state and ends its operation in the OFF state."""
question = f"""What is the MINIMAL number of test cases to achieve valid transitions coverage?"""
options = f"""a) 4 b) 2 c) 7 d) 3 """
instruction = f"""Select ONE option"""


prompt_sys = f"""You are an expert software tester."""
prompt_user = f"""You will be given a question on software testing. Your job is as follows:
                1.Check the info.
                2. Check the diagram.
                3. Check the question.
                4. Choose the option as mentioned in the instruction.
                5. State the reason behind choosing the option.
                
                
                The info is :-```{info}```
                The diagram is :- ```{image_path}```
                The question is :-```{question}```
                The options are :-```{options}```
                The instruction is :- ```{instruction}```
                
                """

my_model = "acntech-genai-se-gpt40"
#client = AzureOpenAI
def get_completion(prompt_sys,prompt_user,model=my_model):
    messages = [{"role": "system","content": prompt_sys},{"role": "user", "content": prompt_user}]
    response = client.chat.completions.create( model="acntech-genai-se-gpt40", # model = "deployment_name",
    messages = messages,
    temperature=0.7,
    max_tokens=2000,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None
    )
    return response.choices[0].message.content.split('\n')



response = get_completion(prompt_sys,prompt_user)
print(response)