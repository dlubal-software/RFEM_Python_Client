from RFEM_prompts import *
import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

# Initialize conversation
conversaton = []

# Example OpenAI Python library request
MODEL = "gpt-4o"

# Conversation loop
while True:
    # Get user message and process prompt
    if len(conversaton) == 0:
        print('\n')
        print(f"\033[{34}m{'I am an AI bot that will help you define your RFEM model. Please give me a general instruction and a description of the model to begin with.'}\033[0m")
        general_instruction = input('\n')        
        processed_instruction = process_prompt(general_instruction)
        conversaton.append({"role": "system", "content": processed_instruction})
        print()
        print(f"\033[{34}m{'Now you can continue defining the different modules of the RFEM model.'}\033[0m")
    user_prompt = input('\n')
    processed_prompt = process_prompt(user_prompt)
    # Add message to conversation
    conversaton.append({"role": "user", "content": processed_prompt})
    # Get ChatGPT answer
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=conversaton,
        temperature=0,
    )
    # Print answer
    assitant_answer = response['choices'][0]['message']['content']
    print()
    print(f"\033[{34}m{assitant_answer}\033[0m")
    # Add answer to conversation
    conversaton.append({"role": "assistant", "content": assitant_answer})