import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

openai_client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY')
)



def get_response_openai(openai_client, prompt, temperature = 0):
    messages = [{'role':"user", 'content':prompt}]
    output = openai_client.chat.completions.create(
    model="gpt-4o-mini",  # Try "gpt-4o-mini" for cheaper option
    messages=messages,
    max_tokens=100,  # Limit response length to save costs
    temperature= temperature
    )
    return output.choices[0].message.content


while True:
    UserInput = input("Ask your ai agent anything, or q,quit to quit !!!!\n")
    if UserInput == 'quit' or UserInput=='q':
        break
    prompt = UserInput
    output = get_response_openai(openai_client, prompt)
    print(output)   
    


