# Flask API for Delivery Prediction

This is a Flask-based API that predicts whether a shipment will be delayed or on time based on input data. The prediction is made using a pre-trained machine learning model.

## Features

- Accepts input through an HTML form.
- Uses a trained model and preprocessed data to make predictions.
- Returns results as either "Delayed" or "On Time."

## Requirements

Before running the application, make sure you have the following installed:

- Python 3.10
- Flask
- pandas
- scikit-learn
- joblib
- seaborn
- matplotlib
- openpyxl

## Setup Instructions

1. Clone the repository or download the code.
2. Place the required files (`scaler.pkl`, `label_encoders.pkl`, `model.pkl`, and `templates/form.html`) in the project directory.
3. Install the required Python libraries:

   ```bash
   pip install flask pandas scikit-learn
   ```

4. Ensure the `form.html` file is in the `templates` folder:

   ```
   project-directory/
   |-- app.py
   |-- scaler.pkl
   |-- label_encoders.pkl
   |-- model.pkl
   |-- templates/
       |-- form.html
   ```

## How to Run

1. Start the Flask development server:

   ```bash
   python app.py
   ```

2. Open your web browser and go to `http://127.0.0.1:5000/`.
3. Fill out the form with the required details:
   - **Origin**: The starting location of the shipment.
   - **Destination**: The destination location of the shipment.
   - **Vehicle Type**: The type of vehicle used for transportation.
   - **Distance (km)**: The distance of the shipment in kilometers.
   - **Weather Conditions**: The weather during transportation.
   - **Traffic Conditions**: The traffic level during transportation.
4. Click "Submit" to get the prediction result.

## Folder Structure

```
project-directory/
|-- app.py                 # Main Flask application
|-- scaler.pkl             # Pre-trained scaler for numerical data
|-- label_encoders.pkl     # Encoders for categorical data
|-- model.pkl              # Pre-trained machine learning model
|-- templates/
    |-- form.html          # HTML form for user input
```

## Notes

- Ensure the pre-trained files (`scaler.pkl`, `label_encoders.pkl`, and `model.pkl`) match the features and transformations used during model training.
- Update the categorical encoding logic in `app.py` if the dataset changes.

## Example Input

- Origin: Delhi
- Destination: Mumbai
- Vehicle Type: Truck
- Distance (km): 1200
- Weather Conditions: Clear
- Traffic Conditions: Light

## Example Output

- "Delayed" or "On Time"

## Troubleshooting

- If you encounter an error related to missing packages, ensure all required libraries are installed.
- Verify that the `.pkl` files are correctly loaded and correspond to your dataset.


## Steps and Decisions
1. Data Preprocessing
- Handling Missing Values:

  Missing values in the 'Vehicle Type' column were handled by randomly imputing them based on the distribution of existing values. This ensures that the dataset is complete without introducing bias from missing data.
Dropping Date Columns:

Columns such as 'Shipment Date', 'Planned Delivery Date', and 'Actual Delivery Date' were dropped. These columns were direct indicators of shipment delays and using them would lead to data leakage, where the model could have access to future information.
Outlier Handling:

The 'Distance (km)' column was cleaned by identifying outliers based on grouping parameters such as 'Origin', 'Destination', 'Vehicle Type', 'Weather Conditions', and 'Traffic Conditions'. Outliers were replaced with the mean distance for that group, ensuring the data's consistency.
Removing Duplicates:

Duplicate rows were removed to ensure the model does not learn from repeated data, which could result in overfitting and inaccurate predictions.
2. Feature Engineering
Label Encoding:
Categorical columns such as 'Origin', 'Destination', 'Weather Conditions', 'Traffic Conditions', and 'Vehicle Type' were transformed into numerical values using Label Encoding. This allows the categorical variables to be used in machine learning models.
3. Model Selection and Training
The data was split into training and testing sets. Two models were considered: Logistic Regression and Random Forest.

Logistic Regression:

Hyperparameter tuning was done using GridSearchCV to find the best combination of parameters like regularization strength ('C'), penalty type, and solver.
Random Forest:

A similar hyperparameter tuning process was applied to optimize parameters like the number of estimators, maximum depth, and split criteria.
4. Model Evaluation
The models were evaluated using the following metrics:

Accuracy: Overall performance of the model.
F1 Score: Balance between precision and recall.
Precision: How many of the predicted delays were actually delayed.
Recall: How many of the actual delays were correctly predicted.
Random Forest outperformed Logistic Regression in all metrics, particularly in precision, where it achieved a perfect score of 1.0. Based on this performance, the Random Forest model was chosen as the final model.

5. Final Model
The best-performing Random Forest model was saved using joblib, allowing it to be loaded and used for future predictions without retraining.
