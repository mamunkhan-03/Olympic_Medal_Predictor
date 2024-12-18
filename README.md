🏅 Olympic Medal Predictor

This project leverages machine learning to predict the number of Olympic medals a country might win. The system provides insights into medal counts based on key features such as the number of participating athletes and previous medal performance by utilizing historical data. Additionally, an interactive web application built with Flask offers real-time predictions based on user input.

🎯 Project Highlights

Accurate Predictions: Employs advanced regression models to forecast medal counts.
Model Evaluation: Compares the performance of various machine learning algorithms.
Interactive Web App: User-friendly interface for inputting data and viewing predictions.

🚀 Key Features

1. Web Application

Simple and intuitive interface.
Accepts inputs like the number of athletes and previous medals won.
Allows users to select a prediction model and view results instantly.

2. Machine Learning Models

Linear Regression: Establishes a direct linear relationship between features and medal counts.
Decision Tree Regressor: Splits data into decision-based nodes for making predictions.
Random Forest Regressor: Combines predictions from multiple decision trees to improve accuracy.
Gradient Boosting Regressor: Sequentially combines weak learners to minimize prediction errors.

3. Data Preprocessing

Outliers such as rows with prev_medals > 400 are manually removed to enhance model performance.
Evaluated models using R² (coefficient of determination) for accuracy.

📂 Project Structure

app.py: Flask application for real-time predictions.
Model/: Directory containing trained machine learning models (.pkl files).
train_models.py: Script for training and saving machine learning models.
templates/: HTML templates for the web application.

📊 Results

The models were trained and tested on historical Olympic data, and their performance was measured using R² scores:

Accuracy of linear_regression = 0.90
Accuracy of decision_tree = 0.85
Accuracy of random_forest = 0.91
Accuracy of gradient_boosting = 0.90



