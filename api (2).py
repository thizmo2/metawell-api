
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI(
    title="MetaWell AI API",
    description="Zulu & Xhosa Translation API",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TranslationRequest(BaseModel):
    text: str
    model: str = "xhosa"  # "xhosa" or "zulu"

@app.post("/translate")
async def translate_text(request: TranslationRequest):
    # Demo translations - replace with your actual models later
    if request.model == "xhosa":
        translations = {
            "hello": "Molo",
            "thank you": "Enkosi", 
            "how are you": "Unjani?",
            "good morning": "Molweni",
            "goodbye": "Sala kakuhle",
            "i love you": "Ndiyakuthanda",
            "please": "Ndicela",
            "sorry": "Uxolo",
            "yes": "Ewe",
            "no": "Hayi",
            "what is your name": "Ngubani igama lakho?",
            "my name is": "Igama lam ngu",
            "where are you from": "Uvelaphi?",
            "i am from": "Ndivela",
            "how much does this cost": "Malini le nto?"
        }
    else:  # zulu
        translations = {
            "hello": "Sawubona",
            "thank you": "Ngiyabonga",
            "how are you": "Unjani?",
            "good morning": "Sawubona",
            "goodbye": "Hamba kahle",
            "i love you": "Ngiyakuthanda",
            "please": "Ngiyacela",
            "sorry": "Uxolo",
            "yes": "Yebo",
            "no": "Cha",
            "what is your name": "Ubani igama lakho?",
            "my name is": "Igama lami ngingu",
            "where are you from": "Uvelaphi?",
            "i am from": "Ngivela",
            "how much does this cost": "Malini lokhu?"
        }
    
    # Simple translation lookup
    input_lower = request.text.lower()
    result = translations.get(input_lower, f"Demo: '{request.text}' in {request.model}")
    
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
            "documentation": "/docs",
            "languages": "xhosa, zulu"
        }
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "MetaWell AI API"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
