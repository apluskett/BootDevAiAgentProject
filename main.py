import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import argparse
from prompts import system_prompt
from call_functions import *


'''
Original Course: Boot.dev - 'Build an AI Agent in Python'
URL: https://www.boot.dev/courses/build-ai-agent-python
Author: Alex Pluskett

This project was built following the above course. 
All course content and curriculum belongs to Boot.dev.
My implementations, refactoring decisions, and extensions are my own work.

Directory structure:
├── calculator
│   ├── main.py
│   ├── pkg
│   │   ├── calculator.py
│   │   └── render.py
│   └── tests.py
├── main.py
├── pyproject.toml
├── README.md
└── uv.lock
└── functions/
    └── get_files_info.py
    └── test_get_files_info.py

Refactoring Notes:
main.py()
- Would extract CLI argument parsing into a cli_commands() function
- Would extract env/API setup into a load_dependencies() function 
- Would extract Gemini logic into a gemini_logic() function
- Kept flat per course assignment constraints

-calculator program came from the course and used mainly as a way to test our agent's abilities.
'''

def main():
    load_dotenv()
    parser = argparse.ArgumentParser(description='Chatbot using Gemini API')
    parser.add_argument("user_prompt", type=str, help='User prompt')
    parser.add_argument("--verbose", action="store_true", help='Enable verbose output')
    args = parser.parse_args()
    api_key = os.environ.get("GEMINI_API_KEY")
    
    if api_key is None:
        raise RuntimeError("GEMINI_API_KEY environment variable not set")
    
    client = genai.Client(api_key=api_key)
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    
    
    for i in range(20):
        function_results = []
        response = client.models.generate_content(model="gemini-2.5-flash", contents=messages, config=types.GenerateContentConfig(system_instruction=system_prompt, tools=[available_functions]))
        checking_cadidate = response.candidates
        if checking_cadidate:
            for candidate in checking_cadidate:
                messages.append(candidate.content)
        if response.usage_metadata is None:
            raise RuntimeError("Response usage metadata is None")
        
        if args.verbose:
            
            if response.function_calls == None:
                print(f'''User prompt: {messages[0].parts[0].text}
    Prompt tokens: {response.usage_metadata.prompt_token_count}
    Response tokens: {response.usage_metadata.candidates_token_count}
    Response: {response.text}''')
                break
            
            else:

                for each in response.function_calls:
                    result_call_function = call_function(each, verbose=True)
                    
                    if not result_call_function.parts:
                        raise RuntimeError("Result of function call is None")
                    
                    if not result_call_function.parts[0].function_response:
                        raise RuntimeError("Result of function call does not contain function response")
                    
                    if not result_call_function.parts[0].function_response.response:
                        raise RuntimeError("Result of function call does not contain function response content")
                    
                    function_results.append(result_call_function.parts[0])
                    print(f'''User prompt: {messages[0].parts[0].text}
    Prompt tokens: {response.usage_metadata.prompt_token_count}
    Response tokens: {response.usage_metadata.candidates_token_count}
    -> {result_call_function.parts[0].function_response.response}
    ''')
        
        else:
            
            if response.function_calls == None:
                print(response.text)
                break
            
            else:
                
                for each in response.function_calls:
                    result_call_function = call_function(each, verbose=False)
                    
                    if not result_call_function.parts:
                        raise RuntimeError("Result of function call is None")
                    
                    if not result_call_function.parts[0].function_response:
                        raise RuntimeError("Result of function call does not contain function response")
                    
                    if not result_call_function.parts[0].function_response.response:
                        raise RuntimeError("Result of function call does not contain function response content")
                    
                    function_results.append(result_call_function.parts[0])
                    print(f"-> {result_call_function.parts[0].function_response.response}")
        messages.append(types.Content(role='user', parts=function_results))
    else:
        print("Reached maximum iterations without a final response.")
        exit(1)
            

if __name__ == "__main__":
    main()
