from flask import Flask,render_template,request
import joblib
from preprocess_review import preprocess

app = Flask(__name__)
model = joblib.load('logistic_regression.pkl')

@app.route("/")
def home():
    return render_template('product_review.html')

@app.route("/reviews", methods = ['POST'])
def result():
    name = request.form.get('name')
    review_text = request.form['review']
    review_clean = [preprocess(review_text)]
    prediction = model.predict(review_clean)
    if prediction == 1:
        sentiment = ", we're happy you like the product, thank you for the positive words."
    else:
        sentiment = ", we would like to apologize for your negative experience, we will contact you regarding this."  
    return render_template('review_result.html', name=name, review_text=review_text, sentiment=sentiment)

if (__name__)=='__main__' :
    app.run(host="0.0.0.0",port=5000)