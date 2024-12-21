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

## License

This project is licensed under the MIT License. Feel free to use and modify it as needed.

