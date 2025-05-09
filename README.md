# Image Classification with CIFAR-10 Dataset and Flask Deployment

## Overview

This project implements an image classification system using a Convolutional Neural Network (CNN) trained on the CIFAR-10 dataset and deploys it as a web application using Flask. The model predicts the class of images from the CIFAR-10 dataset, which includes 10 categories such as airplanes, cars, and animals.

## Project Structure

```
Image-Classification-CNN-Flask
├── app
│   ├── static
│   │   └── styles.css
│   ├── templates
│   │   └── index.html
│   ├── app.py
│   └── model
│       └── cnn_model.keras
├── notebooks
│   └── model_training.ipynb
├── requirements.txt
├── README.md
└── .gitignore
```

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/ahmedelzagh/Image-Classification-CNN-Flask
   cd Image-Classification-CNN-Flask
   ```

2. **Install Dependencies**
   Ensure you have Python 3.x installed. Then, install the required packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

3. **Train the Model**
   Open the Jupyter Notebook located in `notebooks/model_training.ipynb` to design, train, and evaluate the CNN model using the CIFAR-10 dataset. After training, save the model as `cnn_model.keras` in the `app/model` directory.

4. **Run the Flask Application**
   Start the Flask application by running:
   ```bash
   python app/app.py
   ```
   The application will be accessible at `http://127.0.0.1:5000`.

## Usage

- Navigate to the web application in your browser.
- Use the upload form to select an image for classification.
- Submit the form to receive the predicted label for the uploaded image.

## Team

- **Ahmed Hamdy Elzagh** | 21044
- **Alaa Hamdy Abdelrahman** | 21059
- **Abdullah Mohamed Elsayed** | 21071
- **Omar Hesham Eldeeb** | 21097
- **Ahmed Sobhy Elmesarea** | 21106
- **Mohammed Elsayed Atia** | 21201
