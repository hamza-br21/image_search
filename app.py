from flask import Flask, render_template, request
from tensorflow.keras.applications import VGG16
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.vgg16 import preprocess_input, decode_predictions
import numpy as np
from pymongo import MongoClient
import random


client = MongoClient("mongodb://localhost:27017/")
db = client["image_search_db"]
products_collection = db["products"]



app = Flask(__name__)


model = VGG16(weights='imagenet')

@app.route('/')
def index():

    random_products = list(products_collection.aggregate([{"$sample": {"size": 9}}]))
    product_list = [
        {
            "name": product["name"],
            "price": product["price"],
            "image_url": product["image_url"],
            "category": product["category"]
        }
        for product in random_products
    ]
    return render_template('index.html', random_products=product_list, search_done=False)


category_mapping = {
    "cellular_telephone": "smartphone",
    "iPod": "smartphone",
    "digital_watch": "watch",
    "stopwatch": "watch",
    "analog_clock": "watch",
    "reflex_camera": "camera",
    "space_bar": "keyboard",
    "typewriter_keyboard": "keyboard"
}

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return "No file part", 400
    file = request.files['image']
    if file.filename == '':
        return "No selected file", 400

    image_path = f"static/uploads/{file.filename}"
    file.save(image_path)

    predictions = predict_image(image_path)

    predicted_category = predictions[0][1]

    if predicted_category in category_mapping:
        predicted_category = category_mapping[predicted_category]


    predicted_labels = [f"{label}: {round(prob * 100, 2)}%" for (_, label, prob) in predictions]

    similar_products = products_collection.find({"category": predicted_category})

    product_list = []
    for product in similar_products:
        product_list.append({
            "name": product["name"],
            "price": product["price"],
            "image_url": product["image_url"]
        })


    return render_template('index.html', predictions=predicted_labels, products=product_list, category=predicted_category,search_done=True)

def predict_image(image):

    img = load_img(image, target_size=(224, 224))
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)

    img_array = preprocess_input(img_array)

    predictions = model.predict(img_array)

    decoded_predictions = decode_predictions(predictions, top=3)
    return decoded_predictions[0]

if __name__ == '__main__':
    app.run(debug=True)
