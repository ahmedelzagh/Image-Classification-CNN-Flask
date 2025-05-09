import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'  # Disable oneDNN custom operations

from flask import Flask, request, render_template
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)
model = load_model('model/cnn_model.keras')  # Adjusted path to match the training notebook output

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']

    if file.filename == '':
        return "No selected file"

    # Ensure the 'uploads' directory exists
    uploads_dir = 'uploads'
    if not os.path.exists(uploads_dir):
        os.makedirs(uploads_dir)

    img_path = os.path.join(uploads_dir, file.filename)
    file.save(img_path)

    img = image.load_img(img_path, target_size=(32, 32))  # Updated target size to match CIFAR-10 input
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0  # Normalize the image

    prediction = model.predict(img_array)
    predicted_class = np.argmax(prediction, axis=1)

    # Updated class names to match CIFAR-10 dataset
    class_names = [
        'airplane', 'automobile', 'bird', 'cat', 'deer',
        'dog', 'frog', 'horse', 'ship', 'truck'
    ]
    result = class_names[predicted_class[0]]

    return render_template('index.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)