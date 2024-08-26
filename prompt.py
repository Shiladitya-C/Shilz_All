
import Process_Input

file_path = 'C:\Shilz\Shilz_Experiment\APOF.txt' 

requirement = Process_Input.get_file(file_path)
#print(requirement)
def system_prompt():
    prompt_sys = """You are a test manager. Your job is to create test cases from functional requirements. The following rules must be followed :
               1. Combine the information and the rules to test case.
               2. Test cases should cover all the requirements."""
    return prompt_sys

def user_prompt():
    #prompt_user = f"""
    #        The given requirement has information of the new pension and rules which determines if the person is elligible to get the pension.The following needs to be done:-

    #         1. Create 10 positive test cases covering all combination of rules. It is important to cover the entire requirement.
    #         2. The test case should mention the test condition being executed.
    #         3. The test cases should mention the requirement which is being tested.
    #         4. The test case should have the steps mentioned.
    #         5. Every test case should have the expected output.
    #         6. The test cases should be numbered.


    #         Functional Specification : ```{requirement}```` """
    #prompt_user = f"""
    #        The given requirement has information of the new pension and rules which determines if the person is elligible to get the pension.The following needs to be done:-

    #         1. Create 5 negative test cases covering all combination of rules.
    #         2. The rules should be combined together logically to create test cases.
    #         3. The test cases should mention the requirement which is being tested.
    #         4. Every test case should contain the test steps and the sample data which is to be used.
    #         5. Every test case should have the expected output.
    #         6. The test cases should be numbered.


    #         Functional Specification : ```{requirement}```` """
    #prompt_user = f"""
    #        The given requirement has information of the new pension and rules which determines if the person is elligible to get the pension.The following needs to be done:-

    #         1. Create all possible boundary test cases. 
    #         2. Every rule present in the requirement should be considered when creating boundary test cases.
    #         3. The test cases should mention the requirement which is being tested.
    #         4. Every test case should contain the test steps and the sample data which is to be used.
    #         5. Every test case should have the expected output.
    #         6. The test cases should be numbered.

    prompt_user = f"""
            The given requirement has information of the new pension and rules which determines if the person is elligible to get the pension.The following needs to be done:-

             1. Create 10 positive test cases. 
             2. Every rule present in the requirement should be considered when creating the test cases.
             3. The test cases should mention the requirement which is being tested.
             4. Every test case should contain the test steps and the sample data which is to be used.
             5. Every test case should have the expected output.
             6. The test cases should be numbered.                  


             Functional Specification : ```{requirement}```` """
    return prompt_user

