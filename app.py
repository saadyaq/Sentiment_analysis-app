import streamlit as st
import requests
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import numpy as np
from scipy.special import softmax
import joblib as jb

model=jb.load('Sentiment_analysis.pkl')
tokenizer=jb.load('tokenizer.pkl')
def polarity_scores_roberta(example):
    encoded_input=tokenizer(example,return_tensors='pt')
    output=model(**encoded_input)
    scores=output[0][0].detach().numpy()
    scores=softmax(scores)
    scores_dict={
        'roberta_neg': scores[0],
        'roberta_neu': scores[1],
        'roberta_pos': scores[2]    }
    return scores_dict


st.title("Analyse de sentiments avec Roberta")
user_input=st.text_area('Entrez un texte')
if st.button('Analyser'):
    if user_input:
        response = requests.get(f"http://127.0.0.1:8000/analyze?text={user_input}")
        if response.status_code==200:
            scores=response.json()
            scores=polarity_scores_roberta(user_input)
            st.write(f"Score Négatif : {scores['roberta_neg']:.4f}")
            st.write(f"Score Neutre : {scores['roberta_neu']:.4}")
            st.write(f"Score Positif : {scores['roberta_pos']:.4}")
    else:
        st.write("Veuillez entrer un texte!")
