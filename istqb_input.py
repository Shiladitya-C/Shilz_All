import pandas as pd
#import PyPDF2

file_path = 'C:\Shilz\Shilz_Experiment\ISTQB.xlsx'

#input_data = pd.read_excel(file_path)
#print(data.head(5))
def get_sys_prompt():
    s_prompt = """ You are a software tester. You have to answer questions strictly from ISTQB training manual."""
    u_prompt = """ You will be given question, options and instruction. You have to answer every question based on the instruction.
     while answering please consider the following :-
      1. Understand the role associated with the question, for example: tester, test manager, test architect. Answer the question based 
        on the role.
      2. All the questions must be answered based on the instruction given.
      3. The questions should be answered from the knowledge present in ISTQB training material.
      4. For each answer please mention how did you reach the conclusion.
      
      The question is  ```{question}```
      The options are ```{option}```
      The instruction is ```{instruction}```
        """
    return s_prompt,u_prompt
   
def get_data(infile):

    input_data = pd.read_excel(file_path)
    sys_prompt,u_prompt = get_sys_prompt()
    

    return input_data,sys_prompt,u_prompt



 


