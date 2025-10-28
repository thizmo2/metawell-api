
from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI(title="MetaWell AI API", version="1.0")

class TranslationRequest(BaseModel):
    text: str
    model: str = "xhosa"  # "xhosa" or "zulu"

@app.post("/translate")
async def translate_text(request: TranslationRequest):
    # Simple demo - replace with your actual model later
    if request.model == "xhosa":
        translations = {
            "hello": "Molo",
            "thank you": "Enkosi", 
            "how are you": "Unjani?",
            "good morning": "Molweni",
            "goodbye": "Sala kakuhle"
        }
    else:  # zulu
        translations = {
            "hello": "Sawubona",
            "thank you": "Ngiyabonga",
            "how are you": "Unjani?",
            "good morning": "Sawubona",
            "goodbye": "Hamba kahle"
        }
    
    # Simple translation lookup
    input_lower = request.text.lower()
    result = translations.get(input_lower, f"Translation for '{request.text}' not found")
    
    return {
        "success": True,
        "original_text": request.text,
        "translated_text": result,
        "model_used": request.model,
        "api_version": "1.0"
    }

@app.get("/")
async def root():
    return {
        "message": "MetaWell AI API - Zulu & Xhosa Translation",
        "status": "live",
        "endpoints": {
            "translate": "POST /translate",
            "docs": "/docs"
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
