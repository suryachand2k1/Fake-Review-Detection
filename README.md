
# Fake Review Detection Project

## Overview
The Fake Review Detection project employs machine learning and NLP to discern fake online reviews. It offers both a graphical user interface (GUI) and a web-based interface, ensuring versatility and accessibility for different user preferences.

## Dataset (`dataset.csv`)
- **Structure**: CSV format with 'Review' and 'Label'.
- **Contents**: Each entry comprises a review text and its corresponding authenticity label.
- **Preprocessing**: Normalization, tokenization, stopwords removal, lemmatization.

## Machine Learning Models
- **TFIDF (Term Frequency-Inverse Document Frequency)**: Converts text into a numerical representation for machine learning models.
- **EMSVM (Ensemble Model - SVM)**: An ensemble of multiple SVM classifiers for enhanced accuracy.
- **EMNaiveBayes (Ensemble Model - Naive Bayes)**: An ensemble version of the Naive Bayes algorithm.
- **Standard SVM and Naive Bayes**: Baseline models for comparison and training.

## Interfaces

### GUI Application
- Implemented using `tkinter`.
- Features data upload, preprocessing, model training, and result visualization.
- Run via `Main.py`.

### Web Application (`app.py`)
- Developed with the Flask framework.
- Provides a web interface for interacting with the models, including sentiment analysis.
- Incorporates HTML, CSS, and jQuery for frontend; Flask for backend.
- Run via `app.py`.

## Model Management
- `LoadModels.py`: Class-based script for loading serialized machine learning models.
- `Model.py`: Contains the `Model` class, providing an interface for various machine learning models.

## Setup & Installation
1. Install Python 3.x.
2. Install dependencies:
   ```bash
   pip install nltk scikit-learn pandas tkinter flask vaderSentiment matplotlib
   ```
3. Clone the project repository.
4. Ensure serialized model files are available for `LoadModels.py`.

## Running the Applications

### For GUI Application
Run the `Main.py` script:
```bash
python Main.py
```

### For Web Application
Start the Flask server with `app.py`:
```bash
python app.py
```
Access the application through the web browser at the specified port.

## Dependencies
- Python 3.x
- NLTK, Scikit-learn, Pandas
- Tkinter (for GUI)
- Flask (for Web App)
- VaderSentiment (Sentiment Analysis)
- Matplotlib (Data Visualization)

