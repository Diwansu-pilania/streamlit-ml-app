# streamlit-ml-app

##NO2 Prediction Machine Learning Model##

Web App Link:

[Provide your web app link here]

MODEL ACCURACY:


IN PERCENTS : 82 %

Mean Absolute Error (MAE): 3.1067

R-Squared Score (R²): 0.82


OVERVIEW:

This machine learning model is built to predict the NO2 (Nitrogen Dioxide) levels based on various environmental features such as SO2, RSPM, SPM, PM2.5, and other relevant data.


DATASET:


The dataset includes air pollution parameters collected from different locations, including:

State

Location

Agency

Type (Industrial, Residential, etc.)

SO2 (Sulfur Dioxide concentration)

RSPM (Respirable Suspended Particulate Matter)

SPM (Suspended Particulate Matter)

PM2.5 (Particulate matter smaller than 2.5 micrometers)

Year, Month, Day



MODEL TRAINING:



Algorithm Used: Random Forest Regressor

Train-Test Split: 80%-20%

Number of Estimators: 100

Random State: 42




STEPS TO RUN THE MODEL:


Install Dependencies

pip install -r requirements.txt

Run the Streamlit Web App

streamlit run app.py

Enter the required input values in the web app

Click 'Submit' to get NO2 predictions



PROJECT FILES:



app.py: Streamlit web application for user input and predictions.

model.pkl: Trained Random Forest model stored as a pickle file.

data.csv: Dataset used for training and testing.

requirements.txt: List of required dependencies.



HOW THE MODEL WORDS:


The trained model takes user input features through the web app.

It processes the inputs and predicts the NO2 levels.

The result is displayed on the web application interface.



FUTURE IMPROVEMENTS:



Adding more environmental factors for better accuracy.

Implementing time-series forecasting for long-term NO2 predictions.

Deploying the model on a cloud service for scalability.



AUTHOR:



DIWANSU PILANIA 
For any issues or improvements, feel free to contribute or contact me.
