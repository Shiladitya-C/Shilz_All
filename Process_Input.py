import os 
#file_path = 'C:\Shilz\Shilz_Experiment\APOF.txt'
#print(file_path)

def get_file(file_path):

    with open(file_path,'r') as f:
        inp_file = f.readlines()

    #print(inp_file)
    return inp_file

#final_input = get_file(file_path)    