🧠 Sentiment Analysis App — Streamlit Deployment


📘 Overview

This project demonstrates how to build and deploy a Natural Language Processing (NLP) sentiment classification model using TF-IDF vectorization and machine learning algorithms such as Logistic Regression, SVM, and Random Forest.
The model analyzes customer reviews and classifies them into three sentiment categories:

Positive

Neutral

Negative

The interactive Streamlit app allows users to input custom text and view the predicted sentiment in real time.


🧩 Features

✅ Clean and preprocess text reviews
✅ Sentiment labeling based on rating values
✅ Text vectorization using TF-IDF
✅ Model training and evaluation using multiple classifiers
✅ Comparison of model accuracy and F1-scores
✅ Interactive Streamlit dashboard for live sentiment prediction
✅ Deployed directly on Streamlit Cloud


🏗️ Project Structure

📁 sentiment-analyzer/
├── sentiment_app.py          # Main Streamlit application
├── sentiment_model.joblib    # Trained sentiment classifier
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation


⚙️ How to Run Locally

1. Clone this repository
    git clone https://github.com/<your-username>/sentiment-analyzer.git
    cd sentiment-analyzer

2. Install dependencies
    pip install -r requirements.txt

3. Run the Streamlit app
    streamlit run sentiment_app.py


☁️ Deployment (on Streamlit Cloud)

- Push this repository to GitHub.
- Go to https://share.streamlit.io
- Connect your GitHub account and select this repository.
- Set the entry point file as sentiment_app.py.
- Click Deploy — your app will be live in minutes!

📊 Example Predictions
| Review Text                  | Predicted Sentiment |
| ---------------------------- | ------------------- |
| "Battery drains too fast"    | Negative            |
| "Camera quality is amazing!" | Positive            |
| "It’s okay for the price"    | Neutral             |


📚 Tech Stack

- Python 3.10+
- Streamlit
- Scikit-learn
- Pandas & NumPy
- Joblib
- NLTK / WordCloud


👨‍💻 Author
Daniel Saputro