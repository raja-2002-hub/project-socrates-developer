# importing  core FastAPI modules
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
# importing custom modules for Socratic response, NLP processing, and prediction
from app.socrates import generate_response
from app.nlp_utils import preprocess_input
from app.predictor import predict_category  


# creating  a FastAPI instance
app = FastAPI()


 # POST route at "/ask" to handle incoming questions from frontend
@app.post("/ask")
async def ask(request: Request):
    try:
        # Parsing JSON body from incoming request
        data = await request.json()

        # Extracting the 'question' field from request
        question = data.get("question", "")
        print(f"User question: {question}")
        
         # Validate input (rejecting empty questions)
        if not question.strip():
            return JSONResponse(content={"error": "Empty question"}, status_code=400)
        
        # Preprocessing  question using NLP (tokenize, lemmatize, clean)
        cleaned = preprocess_input(question)
        print(f"Cleaned: {cleaned}")

        # Predicting the category and get confidence score from the ML model
        category, confidence = predict_category(cleaned)
        print(f"Predicted Category: {category} (Confidence: {confidence})")
        

        # Generate a Socratic-style answer using OpenAI GPT
        response = generate_response(cleaned)
        print(f"GPT Response: {response}")
        
        # response to frontend as JSON
        return {
            "category": category,
            "confidence": confidence,
            "answer": response
        }

    except Exception as e:

        # Catch and log any runtime errors for debugging
        import traceback
        traceback.print_exc()
        # Returning  a user friendly error message
        return JSONResponse(content={"error": f"Internal server error: {e}"}, status_code=500)

# Mounting  the frontend HTML interface (index.html) from the 'frontend/' folder
app.mount("/", StaticFiles(directory="frontend", html=True), name="static")
