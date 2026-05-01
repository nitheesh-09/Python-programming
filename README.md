# 🚗 License Plate Recognition System (ANPR)

## 📌 Overview
This project is a License Plate Recognition System developed using Python, OpenCV, and TensorFlow/Keras.  
It automatically detects and recognizes vehicle license plate characters from images using Deep Learning (CNN).

---

## 🎯 Objective
- To automate vehicle number identification  
- To reduce manual effort in traffic systems  
- To demonstrate the use of AI + Image Processing in real-world applications  

---

## 🛠️ Technologies Used
- Python  
- OpenCV (cv2)  
- NumPy  
- TensorFlow / Keras  
- Pillow (PIL)  
- Matplotlib  

---

## ⚙️ Project Modules
1. Dataset Generation  
   - Creates alphanumeric character dataset (A–Z, 0–9)

2. Model Training  
   - Trains CNN model using generated dataset

3. Plate Prediction  
   - Detects and predicts characters from license plate image

---

## 🔄 Workflow
Dataset Generation → Model Training → Image Input → Preprocessing → Character Segmentation → Prediction → Output

---

## 📷 Sample Input
![Input Image](images/input.png)

---

## 📤 Sample Output
Detected Plate: KL07AB1234

---

## 🚀 How to Run

### Step 1: Clone the repository
git clone https://github.com/your-username/python-programming.git  
cd python-programming  

### Step 2: Install dependencies
pip install opencv-python tensorflow numpy pillow matplotlib  

### Step 3: Generate dataset
python generate_dataset.py  

### Step 4: Train model
python train_plate.py  

### Step 5: Run prediction
python predict_plate.py  

---

## 📊 Features
- Automatic license plate recognition  
- Fast and efficient system  
- Uses Deep Learning (CNN)  
- Scalable for real-time applications  

---

## 🌍 SDG Mapping
SDG 9 – Industry, Innovation, and Infrastructure  

This project supports smart infrastructure by:
- Enabling automated traffic systems  
- Improving efficiency in transportation  
- Promoting AI-based innovations  

---

## 📚 Research Reference
Anagnostopoulos, C. N. E., et al.  
“License Plate Recognition from Still Images and Video Sequences: A Survey”  
IEEE Transactions on Intelligent Transportation Systems, 2008.

---

## 🔮 Future Enhancements
- Real-time video processing  
- Integration with CCTV cameras  
- Improved accuracy with larger datasets  
- Use of advanced object detection models (YOLO, etc.)  

---

## 👨‍💻 Author
Your Name  

---

## ⭐ Acknowledgment
This project is developed as part of a Python Mini Project to demonstrate practical implementation of AI and image processing.
