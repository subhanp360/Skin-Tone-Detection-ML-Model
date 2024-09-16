# Human Skin Tone Classification

This project is a machine learning application that classifies human skin tones using a trained model. It includes a web interface where users can upload an image (in JPG format) and the app will predict the skin tone based on a pre-trained model.

## Project Structure

```
/Skin Tone Detection Model Project/
│
├── /src/                   # Flask app for prediction
│   └── app.py              # Main backend script
├── /web/                   # Frontend HTML interface
│   └── index.html          # Webpage for image upload and result display
├── /models/                # Trained models folder
│   └── skin_tone_model.h5  # Pretrained model for skin tone classification
├── /data/                  # Data folder (optional)
├── requirements.txt        # Dependencies file
└── README.md               # Project instructions
```

## Getting Started

To get the app running locally, follow these steps:

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ML-Project.git
cd ML-Project
```

### 2. Install Dependencies

You can install all required Python packages by running:

```bash
pip install -r requirements.txt
```

### 3. Running the Backend (Flask API)

To run the backend application, execute the following command:

```bash
python src/app.py
```

This will start a local server. The prediction API will be available at `http://127.0.0.1:5000/predict`.

### 4. Running the Frontend (HTML Page)

1. Open `web/index.html` in your browser.
2. This will display a simple webpage with an image upload form.
3. Click the **"Upload"** button and select a **JPG image**.
4. Hit the **"Submit"** button.

The app will send the image to the Flask backend API for prediction, and the result will be displayed on the page.

### 6. Example Output

After uploading the image, the result (predicted skin tone) will be displayed in the browser.

### Example prediction results:
- "Black"
- "Brown"
- "White"

## Model

The project uses a **pre-trained skin tone classification model** stored in `models/skin_tone_model.h5`. The model was trained on the [Human Faces Dataset](https://www.kaggle.com/datasets/ashwingupta3012/human-faces/data).

## Acknowledgements

- Dataset provided by [Ashwin Gupta](https://www.kaggle.com/ashwingupta3012) on [Kaggle](https://www.kaggle.com/datasets/ashwingupta3012/human-faces/data).