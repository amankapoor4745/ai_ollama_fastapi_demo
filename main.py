# server.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from langchain_ollama import OllamaLLM
import warnings
from urllib3.exceptions import NotOpenSSLWarning

warnings.filterwarnings("ignore", category=NotOpenSSLWarning)

load_dotenv()  # loads .env in the same folder

API_KEY = os.getenv("Ollama_API_KEY")  # read from .env

app = FastAPI()
llm = OllamaLLM(model="mistral")  # initialize once

class QueryRequest(BaseModel):
    query: str
    api_key: str

@app.post("/ask")
def handle_query(request: QueryRequest):
    if request.api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")
    response = llm.invoke(request.query)
    return {"response": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)