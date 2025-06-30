import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

# if there is no argument provided aftering running the program
if len(sys.argv) < 2:
    print("Error: No prompt provided.")
    sys.exit(1)

if sys.argv[1] == "":
    print("Error: Empty prompt")
    sys.exit(1)

user_prompt = sys.argv[1] 

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

#LLM Call + Response
response = client.models.generate_content(
    model='gemini-2.0-flash-001',
    contents=messages,
    )

if "--verbose" in sys.argv:
    print(f"User prompt: {user_prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
     
else:
    print(response.text)


