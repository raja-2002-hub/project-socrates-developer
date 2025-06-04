import openai
import os
from dotenv import load_dotenv

# Load all variables from .env into the environment
load_dotenv()
# Reading  the OpenAI API key from the environment
api_key = os.getenv("OPENAI_API_KEY")

# If the API key is missing, raise an error and stop execution
if not api_key:
    raise RuntimeError("❌ OPENAI_API_KEY not found. Please check your .env file.")

openai.api_key = api_key

# Defining  a function to call the GPT model with a given prompt
def call_llm(prompt: str) -> str:
    try:
          # Call the GPT gpt-4o with a system prompt and user message
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are Socrates, a philosopher who answers with deep and reflective questions."},
                {"role": "user", "content": prompt}
            ]
        )
        # Extract the assistant's message from the response and return it
        return response.choices[0].message.content.strip()
    
    # If any error occurs return an error message
    except Exception as e:
        return f"Error contacting LLM API: {e}"
