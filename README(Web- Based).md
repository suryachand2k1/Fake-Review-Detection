# Fake Review Detection Project

## Overview
The Fake Review Detection project utilizes machine learning and NLP to identify fake online reviews, implemented as a Flask web application. This project aims to assist in maintaining the credibility of online review systems.

## Dataset (`dataset.csv`)
- **Structure**: CSV format with 'Review' and 'Label'.
- **Contents**: Review text with corresponding labels (genuine or fake).
- **Preprocessing**: Includes normalization, tokenization, stopwords removal, lemmatization.

## Machine Learning Models
- **TFIDF**: Text to weighted vector representation.
- **EMSVM (Ensemble Model - SVM)**: Combines multiple SVM classifiers.
- **EMNaiveBayes (Ensemble Model - Naive Bayes)**: Ensemble Naive Bayes algorithm.
- **SVM and Naive Bayes**: Baseline models for comparison.

## Web Application (`app.py`)
- **Framework**: Flask.
- **Features**: Web interface for model interaction, Sentiment Analysis integration.
- **Frontend**: Basic HTML and CSS with jQuery for REST calls.
- **Backend**: Flask server handling requests and model operations.

## Model Management
- `LoadModels.py`: Class-based approach to load serialized models using `pickle`.
- `Model.py`: Defines `Model` class for handling different ML models.

## Setup & Installation
1. Install Python 3.x and Flask.
2. Install dependencies:
   ```bash
   pip install nltk scikit-learn pandas flask vaderSentiment matplotlib
   ```
3. Clone the repository.
4. Ensure model files are ready for `LoadModels.py`.

## Running the Application
Start the Flask app:
```bash
python app.py
```
Access the web interface on the designated port for interacting with the models.

## Dependencies
- Python 3.x
- NLTK, Scikit-learn, Pandas
- Flask (Web framework)
- VaderSentiment (Sentiment Analysis)
- Matplotlib (Visualization)
