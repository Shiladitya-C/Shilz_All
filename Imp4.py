import os
from dotenv import load_dotenv
load_dotenv('C:\Shilz\Shilz_Experiment\Shilz_Exp_2\my_secret_GPT4o.env')

my_variable = os.getenv('SECRET_KEY')

def get_imp():
    end_point = "https://acntech-genai-se.openai.azure.com/"
    key = my_variable
    api_version = "2024-02-15-preview"

    return end_point,key,api_version

ep,k,api = get_imp()
print(f"end point is : {ep}")
print(f"key is : {k}")
print(f"api : {api}")


