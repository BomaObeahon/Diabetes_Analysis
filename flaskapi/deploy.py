from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load the model
with open('random_forest_model.pkl', 'rb') as file:
    rf_model = pickle.load(file)

@app.route('/predict', methods=['POST'])
def predict():
    # Get input data from request
    data = request.get_json(force=True)

    # Make predictions
    input_data = data.get('input_data')  # Assuming 'input_data' is the key for input data
    prediction = rf_model.predict(input_data)

    # Return the prediction as JSON response
    return jsonify({'prediction': prediction.tolist()})

@app.route('/')  # Handle requests to the root URL
def index():
    return 'Welcome to the Diabetes Prediction API!'

if __name__ == '__main__':
    app.run(debug=True)

    
