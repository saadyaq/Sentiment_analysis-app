from fastapi import FastAPI,Query
import joblib as jb
from transformers import AutoTokenizer, AutoModelForSequenceClassification



import numpy as np
from scipy.special import softmax

app=FastAPI()

model = jb.load('Sentiment_analysis.pkl')
tokenizer = jb.load('tokenizer.pkl')

def polarity_scores_roberta(example):
    encoded_input=tokenizer(example,return_tensors='pt')
    output=model(**encoded_input)
    scores=output[0][0].detach().numpy()
    scores=softmax(scores)
    scores_dict={
        'roberta_neg': float(scores[0]),
        'roberta_neu': float(scores[1]),
        'roberta_pos': float(scores[2])    }
    return scores_dict
#API operations
@app.get("/")
def health_check():
    return {"message": "Hello, World!"}

@app.get("/analyze")
def analyze_sentiment(text:str=Query(...)):
    scores=polarity_scores_roberta(text)
    return scores