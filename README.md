# 🎬 Movie Review Sentiment Analysis
**LIVE DEMO:** Click Here [https://movie-review-nlp-project.streamlit.app/]

A Natural Language Processing (NLP) project that classifies IMDB movie reviews as **Positive** or **Negative** using a Logistic Regression model with TF-IDF vectorization. Includes an interactive **Streamlit** web app for real-time predictions.

---

## 📌 Project Overview

This project uses the IMDB Dataset (50,000 reviews) to train a sentiment classification model. The trained model is then deployed as a user-friendly web application where anyone can enter a movie review and instantly get a sentiment prediction along with a confidence score.

---

## 🚀 Demo

> Enter a movie review → Click **Predict** → Get Positive 😊 or Negative 😞 result with confidence %

---

## 🗂️ Project Structure

```
movie-sentiment-analysis/
│
├── sentimental_analysis_using_streamlid.ipynb   # Model training notebook
├── app.py                                        # Streamlit web application
├── IMDB_Dataset.csv                              # Dataset (50K reviews)
├── sentiment_model.pkl                           # Saved Logistic Regression model
├── tfidf_vectorizer.pkl                          # Saved TF-IDF vectorizer
├── requirements.txt                              # Python dependencies
└── README.md                                     # Project documentation
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data loading and preprocessing |
| Scikit-learn | TF-IDF vectorization & Logistic Regression |
| Joblib | Model serialization (.pkl files) |
| Streamlit | Web application interface |
| Matplotlib | Confidence pie chart visualization |

---

## 📊 Model Details

- **Dataset:** IMDB Dataset — 50,000 movie reviews (balanced: 25K positive, 25K negative)
- **Features:** TF-IDF Vectorizer with `max_features=5000`
- **Model:** Logistic Regression
- **Train/Test Split:** 80% / 20%
- **Evaluation Metrics:** Accuracy Score, Confusion Matrix, Classification Report

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/movie-sentiment-analysis.git
cd movie-sentiment-analysis
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Train the model (generates .pkl files)

Open and run the Jupyter notebook:

```bash
jupyter notebook sentimental_analysis_using_streamlid.ipynb
```

Run all cells — this will generate `sentiment_model.pkl` and `tfidf_vectorizer.pkl` in your project folder.

### 5. Run the Streamlit app

```bash
streamlit run app.py
```

Then open your browser at `http://localhost:8501`

---

## 📝 Requirements

Create a `requirements.txt` with the following:

```
pandas
scikit-learn
streamlit
joblib
matplotlib
jupyter
```

---

## 🖥️ How to Use

1. Launch the app with `streamlit run app.py`
2. Type or paste any movie review into the text box
3. Click the **Predict** button
4. View the sentiment result (Positive/Negative), confidence score, and word/character count

---

## 📈 Results

| Metric | Score |
|---|---|
| Accuracy | ~89% |
| Model | Logistic Regression |
| Vectorizer | TF-IDF (5000 features) |

---

## 📁 Dataset

The [IMDB Dataset](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews) contains 50,000 movie reviews labeled as positive or negative. It is included in this repository as `IMDB_Dataset.csv`.


---

## 🙋‍♂️ Author
- GitHub: https://github.com/abirami-1506
- LinkedIn: https://www.linkedin.com/in/abiramibalaji1506

---

## 📄 License
This project is open source and available under the [MIT License](LICENSE).
