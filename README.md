# Sentiment Analysis App

## Description
Cette application utilise le modèle **Roberta** pré-entraîné pour effectuer une analyse de sentiments sur du texte donné par l'utilisateur. Grâce à **Streamlit**, vous pouvez entrer un texte et obtenir des résultats de sentiment (négatif, neutre ou positif) directement depuis une interface web simple.

## Fonctionnalités
- **Entrée de texte utilisateur** : L'utilisateur peut entrer n'importe quel texte.
- **Analyse de sentiments** : L'application utilise un modèle **Roberta** pour calculer les probabilités de sentiment (négatif, neutre, positif).
- **Interface web simple** : L'application est développée avec **Streamlit**, permettant une interface rapide et facile à utiliser.

## Installation

1. Clonez le dépôt :
    ```bash
    git clone https://github.com/votre_nom_utilisateur/sentiment-analysis-app.git
    ```

2. Installez les dépendances :
    ```bash
    pip install -r requirements.txt
    ```

3. Lancez l'application Streamlit :
    ```bash
    streamlit run app.py
    ```

## Dépendances
- `transformers`
- `torch`
- `streamlit`
- `joblib`
- `numpy`
- `scipy`

Vous pouvez installer toutes les dépendances en utilisant le fichier `requirements.txt`.

## Exemple d'utilisation
1. Entrez un texte dans l'interface.
2. Cliquez sur "Analyser" pour voir les résultats de l'analyse de sentiments (négatif, neutre, ou positif).

![Exemple d'interface](screenshot.png)

## Fichiers importants
- **app.py** : Script principal de l'application Streamlit.
- **sentiment_model.pkl** : Modèle Roberta pré-entraîné pour l'analyse de sentiments.
- **tokenizer.pkl** : Tokenizer Roberta utilisé pour transformer les textes en tokens.


## License
Ce projet est sous licence MIT. Voir [LICENSE](LICENSE) pour plus d'informations.
