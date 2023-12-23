
# Fake Review Detection Project

## Overview
The Fake Review Detection project utilizes advanced machine learning and natural language processing techniques to classify online reviews as genuine or fake. This project aims to assist in maintaining the credibility of online review systems by identifying fraudulent reviews.

## Dataset (`dataset.csv`)
- **Structure**: The dataset is structured in CSV format with two columns: 'Review' and 'Label'.
- **Contents**: Each entry contains a review text and its corresponding label (indicative of the review being genuine or fake).
- **Preprocessing Steps**:
  - Text normalization to lower case.
  - Tokenization to convert sentences into words.
  - Removal of stopwords and punctuations.
  - Application of lemmatization techniques for reducing words to their base or root form.

## Machine Learning Models
- **TFIDF (Term Frequency-Inverse Document Frequency)**: Converts text into a weighted vector representation, emphasizing important words.
- **EMSVM (Ensemble Model - Support Vector Machine)**: A composite model that combines multiple SVM classifiers for improved prediction accuracy.
- **EMNaiveBayes (Ensemble Model - Naive Bayes)**: An ensemble version of the Naive Bayes algorithm, known for its effectiveness in text classification.
- **SVM (Support Vector Machine)**: A baseline SVM model for comparison and ensemble training.
- **Naive Bayes**: A probabilistic model that applies Bayes' theorem with strong independence assumptions between features.

## Scripts Overview
- `LoadModels.py`: Responsible for loading serialized machine learning models using Python's `pickle` module. It initializes the models in the `Model` class.
- `Main.py`: The main script for the project's graphical user interface (GUI) using `tkinter`. It includes functionalities for data upload, preprocessing, model training, and visualization of results.
- `Model.py`: Defines the `Model` class with methods for setting and retrieving different machine learning models used in the project.
- `run.py`: A script that demonstrates the usage of loaded models to analyze and classify review texts. It showcases how the models can be employed for sentiment analysis and review classification.

## Setup & Installation
1. Ensure Python 3.x is installed on your system.
2. Install necessary Python libraries:
   ```bash
   pip install nltk scikit-learn pandas tkinter vaderSentiment matplotlib
   ```
3. Clone or download the project repository to your local machine.
4. Ensure the serialized model files are present in the project directory for `LoadModels.py` to function properly.

## Running the Application
To start the application, run the `Main.py` script:
```bash
python Main.py
```
This will open the GUI, where you can upload the dataset, preprocess the data, train models, and view the classification results.

## Dependencies
- Python 3.x
- NLTK (Natural Language Toolkit)
- Scikit-learn (Machine Learning library)
- Pandas (Data manipulation and analysis)
- Tkinter (Standard GUI library for Python)
- VaderSentiment (Sentiment Analysis tool)
- Matplotlib (Data visualization)

