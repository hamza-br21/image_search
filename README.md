# 🔍 Image-Based Product Search with AI & MongoDB

Welcome to **Image-Based Product Search**, a web application that allows users to find similar products by uploading an image. This project leverages **deep learning (VGG16), Flask, MongoDB, and Docker** to provide a seamless experience for e-commerce platforms. 🚀

## 📸 Features
- ✅ Upload an image to search for similar products
- ✅ AI-powered **image classification** using **VGG16** (TensorFlow)
- ✅ **MongoDB** for product storage and retrieval
- ✅ **Flask** backend for handling requests and predictions
- ✅ Responsive **Bootstrap** front-end
- ✅ **Docker support** for easy deployment

---

## 🛠️ Tech Stack
- **Backend:** Flask (Python) 🐍
- **Deep Learning:** TensorFlow (VGG16) 🧠
- **Database:** MongoDB 🗃️
- **Frontend:** HTML, CSS (Bootstrap) 🎨
- **Containerization:** Docker 🐳

---

## 🚀 Installation & Setup

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/hamza-br21/image_search.git
cd image_search
```

### **2️⃣ Set Up a Virtual Environment (Recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Start MongoDB (Using Docker)**
```bash
docker run -d --name mongodb -p 27017:27017 mongo
```

### **5️⃣ Run the Flask App**
```bash
python app.py
```

📍 Open `http://127.0.0.1:5000/` in your browser.

---

## 📂 Project Structure
```plaintext
📦 image_search
├── 📂 static            # Contains uploaded images & styles
│   ├── 📂 uploads      # Uploaded product images
│   ├── 📂 css          # Stylesheets
│   ├── ...
├── 📂 templates         # HTML files (Flask templates)
│   ├── index.html      # Main interface
├── app.py              # Flask application
├── requirements.txt    # Dependencies
├── README.md           # Project documentation
```

## 🔥 How It Works
1️⃣ User uploads an image of a product 📸
2️⃣ The image is processed by **VGG16** to classify its category 🧠
3️⃣ **MongoDB** searches for similar products in its database 🗃️
4️⃣ The results are displayed on the web interface with product details 🛒

---

## 🐳 Deploying with Docker
For easier deployment, you can use Docker:
```bash
docker build -t image_search .
docker run -p 5000:5000 image_search
```
Then access `http://127.0.0.1:5000/`.

---

