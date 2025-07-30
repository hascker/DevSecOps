from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from textblob import TextBlob

app = FastAPI()

class TextRequest(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the Sentiment Analyzer API"}

@app.post("/analyze/")
def analyze_sentiment(request: TextRequest):
    if not request.text:
        raise HTTPException(status_code=400, detail="Text cannot be empty")
    
    analysis = TextBlob(request.text)
    sentiment = analysis.sentiment.polarity

    sentiment_label = (
        "positive" if sentiment > 0 else "negative" if sentiment < 0 else "neutral"
    )

    return {
        "text": request.text,
        "polarity": sentiment,
        "sentiment": sentiment_label
    }

