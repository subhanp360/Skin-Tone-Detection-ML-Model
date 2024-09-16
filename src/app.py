from flask import Flask, request, jsonify
from flask_cors import CORS
from tensorflow.keras.models import load_model # type: ignore
import numpy as np
from tensorflow.keras.preprocessing import image # type: ignore
from PIL import Image
import io

app = Flask(__name__)
CORS(app)  # Enable CORS

# Load the model
model_path = 'C:/users/project/desktop/subhan_work/skin_tone_model.h5'
model = load_model(model_path)

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the prediction API. Use the /predict endpoint to get predictions."

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Check if the file is in the request
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400

        file = request.files['file']
        
        # Read the image in a way that load_img can handle
        img = Image.open(io.BytesIO(file.read()))
        
        # Resize the image to the target size
        img = img.resize((150, 150))
        
        # Convert the image to an array
        img_array = image.img_to_array(img)
        
        # Expand the dimensions to match the input shape of the model
        img_array = np.expand_dims(img_array, axis=0)
        
        # Normalize the image array
        img_array /= 255.0
        
        # Make a prediction
        predictions = model.predict(img_array)
        predicted_class = np.argmax(predictions[0])
        
        # Map the prediction to a descriptive label
        if predicted_class == 0:
            result = "Black"
        elif predicted_class == 1:
            result = "Brown"
        elif predicted_class == 2:
            result = "White"
        else:
            result = "Unknown"

        return jsonify({'prediction': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
