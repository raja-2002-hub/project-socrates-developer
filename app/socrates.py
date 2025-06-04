
# Importing  the function that calls the GPT-4 API
from app.llm_api import call_llm

# Defining  a function to generate a Socratic style response
def generate_response(question: str) -> str:

    # Constructing  a prompt that frames the user's question as input to Socrates
    prompt = f"As Socrates, respond with thoughtful inquiry to the following:\n\n{question}"

     # Call the  GPT-4 to generate a response based on the prompt
    return call_llm(prompt)
