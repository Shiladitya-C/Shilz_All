import openai
import Imp
#import prompt
import istqb_input
from openai import AzureOpenAI

endpoint , key,api_v = Imp.get_imp()

client = AzureOpenAI(
  azure_endpoint = endpoint, 
  api_key=key,  
  api_version= api_v
)

#prompt_sys = prompt.system_prompt()
#prompt_user = prompt.user_prompt()

input_data,prompt_sys,prompt_user = istqb_input.get_data()


my_model = "grumpy-model"
def get_completion(prompt_sys,prompt_user,model=my_model):
    messages = [{"role": "system","content": prompt_sys},{"role": "user", "content": prompt_user}]
    response = client.chat.completions.create( model="grumpy-model", # model = "deployment_name",
    messages = messages,
    temperature=0.7,
    max_tokens=2000,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None
    )
    return response.choices[0].message.content.split('\n')

def process_input(input_data):
    inp = input_data
    for index, row in input_data.iters():
        question = question
        



response = get_completion(prompt_sys,prompt_user)
print(response)
#out_path = 'C:\Shilz\Shilz_Experiment\out_positive.txt'
#out_path = 'C:\Shilz\Shilz_Experiment\out_negative.txt'
#out_path = 'C:\Shilz\Shilz_Experiment\out_boundary.txt'
out_path = 'C:\Shilz\Shilz_Experiment\coverage.txt'

with open(out_path,'w') as f:
     for r in response:
        f.write(f"{r} + \n")