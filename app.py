from flask import Flask, render_template, request
import pickle
import pandas as pd
import os

app = Flask(__name__)


model_files = {
    'linear_regression': os.path.join('Model', 'linear_regression_model.pkl'),
    'decision_tree': os.path.join('Model', 'decision_tree_model.pkl'),
    'random_forest': os.path.join('Model', 'random_forest_model.pkl'),
    'gradient_boosting': os.path.join('Model', 'gradient_boosting_model.pkl')
}

# Function to load the model from a pickle file
def load_model(model_name):
    model_path = model_files.get(model_name)
    if model_path and os.path.exists(model_path):
        with open(model_path, 'rb') as file:
            return pickle.load(file)
    else:
        raise FileNotFoundError(f"Model file not found for {model_name}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        athletes = float(request.form['athletes'])
        prev_medals = float(request.form['prev_medals'])
        selected_model = request.form['model']

    
        model = load_model(selected_model)

    
        input_data = pd.DataFrame([[athletes, prev_medals]], columns=["athletes", "prev_medals"])

       
        prediction = model.predict(input_data)[0]

        
        return render_template('index.html', result=round(prediction, 2))

    except Exception as e:
        
        return render_template('index.html', result=f"Error: {e}")

if __name__ == '__main__':
    app.run(debug=True)
