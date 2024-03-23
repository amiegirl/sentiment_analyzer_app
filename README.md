# Sentiment Analysis of Real-time Flipkart Product Reviews

## Objective
The objective of this project is to classify customer reviews as positive or negative and understand the pain points of customers who write negative reviews.
By analyzing the sentiment of reviews, we aim to gain insights into product features that contribute to customer satisfaction or dissatisfaction.

## Dataset
A team of Data Engineers have already scraped real-time data from Flipkart website.
Click [Here](https://drive.google.com/file/d/1Nh3uBJcMATZT0WVTVokBKc3SDvIpl9Vt/view?usp=sharing) to download the data.

The dataset consists of 8,518 reviews for the "YONEX MAVIS 350 Nylon Shuttle" product from Flipkart.
Each review includes features such as Reviewer Name, Rating, Review Title, Review Text, Place of Review, Date of Review, Up Votes, and Down Votes.

## Data Preprocessing
1. Text Cleaning: Remove special characters, punctuation, and stopwords from the review text.
2. Text Normalization: Perform lemmatization or stemming to reduce words to their base forms.
3. Numerical Feature Extraction: Apply techniques like Bag-of-Words (BoW),
4. Term Frequency-Inverse Document Frequency (TF-IDF), Word2Vec (W2V), and BERT models for feature extraction.

### Positive reviews
![image](https://github.com/amiegirl/sentiment_analyzer_app/assets/81017006/2cc62a0a-91ff-44b9-846b-cca73c25c2a5)<br>

### Negative reviews
![image](https://github.com/amiegirl/sentiment_analyzer_app/assets/81017006/610aca57-9973-42eb-bcbf-a23eeb188aff)<br>

## Modeling Approach
1. Model Selection: Train and evaluate various machine learning and deep learning models using the embedded text data.
2. Evaluation Metric: Use the F1-Score as the evaluation metric to assess the performance of the models in classifying sentiment.


## Model Deployment
1. Flask or Streamlit App Development: Develop a Flask or Streamlit web application that takes user input in the form of a review and generates the sentiment (positive or negative) of the review.
2. Model Integration: Integrate the trained sentiment classification model into the Flask for real-time inference.
3. Deployment: Deploy the Flask app on an AWS EC2 instance to make it accessible over the internet.<br>

https://github.com/amiegirl/sentiment_analyzer_app/assets/81017006/9b51f625-8403-479e-abee-fbff4b6f11da

## Testing and Monitoring Test the deployed application and monitor its performance for any issues or errors.
