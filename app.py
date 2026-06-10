import streamlit as st
import joblib
import matplotlib.pyplot as plt
model = joblib.load("sentiment_model.pkl")
tfidf = joblib.load("tfidf_vectorizer.pkl")
st.title("🎬 Movie Review Sentiment Analysis")
st.write("Enter a movie review and check whether it is Positive or Negative.")
review = st.text_area("Enter your review:")
if st.button("Predict"):

    if review.strip() == "":
        st.warning("Please enter a review.")
    else:
        review_tfidf = tfidf.transform([review])

        prediction = model.predict(review_tfidf)

        probability = model.predict_proba(review_tfidf)
        confidence = probability.max() * 100

        if prediction[0] == 1:
            st.balloons()
            st.success(f"😊 Positive Review\n\nConfidence: {confidence:.2f}%")
        else:
            st.error(f"😞 Negative Review\n\nConfidence: {confidence:.2f}%")
        fig, ax = plt.subplots()

        ax.pie(
            [confidence, 100 - confidence],
            labels=["Confidence", "Remaining"],
            autopct="%1.1f%%"
        )
        st.pyplot(fig)

        st.write(f"Word Count: {len(review.split())}")
        st.write(f"Character Count: {len(review)}")










        