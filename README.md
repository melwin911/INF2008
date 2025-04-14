# **P5-7-INF2008 Machine Learning**

##   📌 Project Overview
This project focuses on **image classification** using **machine learning models**. It includes:
- **Dataset Preparation**: Merging datasets and augmenting images (already completed).
- **Feature Extraction**: Using a Convolutional Neural Network (CNN) to extract meaningful representations.
- **Machine Learning Models**: Training classifiers such as **K-Nearest Neighbors (KNN)**, **Random Forest (RF)**, and **Support Vector Machine (SVM)** on CNN features.

## 📁 Directory Structure
├── new_dataset/ # Final merged dataset (ready to use)  
├── augment_image.py # Image augmentation script (already applied)  
├── merge_dataset.py # Dataset merging script (already executed)  
├── knn_cnn_features.ipynb # KNN classifier using CNN features  
├── rf_cnn_features.ipynb # Random Forest classifier using CNN features  
├── svm_cnn_features.ipynb # SVM classifier using CNN features  
├── requirements.txt # Dependencies  
└── README.md # Project Documentation

## ⚡ Getting Started

### 1️⃣ Install Dependencies
Run the following command to install the required packages:
```bash
pip install -r requirements.txt
```

### 2️⃣ Extract Features Using CNN
Feature extraction is performed inside the Jupyter notebooks (.ipynb files).  
A pretrained CNN model (VGG16) extracts deep features from images.

### 3️⃣ Verify the Installation
Ensure everything is set up correctly by listing the installed packages:  
```bash
pip list
```

### 4️⃣ Required VSCode Extensions
For working with Jupyter Notebooks (.ipynb) in VSCode, ensure the following extensions are installed:  

1. Python Extension (Microsoft): Provides support for running Python scripts.  
2. Jupyter Extension (Microsoft): Enables support for editing and running Jupyter Notebooks.  
3. Pylance Extension (Microsoft): Provides fast and feature-rich Python language support, including IntelliSense and type checking.

You may install all of these via the VSCode Marketplace.

### 5️⃣ Train Machine Learning Models
Each .ipynb notebook trains a different classifier:  

K-Nearest Neighbors (KNN): knn_cnn_features.ipynb  
Random Forest (RF): rf_cnn_features.ipynb  
Support Vector Machine (SVM): svm_cnn_features.ipynb

## 🤖 Authors & Contributions
[Owen Nyo Wei Yuan] - Data Preprocessing & Augmentation  
[Chai Jun Yu] - Model Implementation & Training  
[Neo Zhiyong] - Feature Engineering & CNN Implementation  
[Chia Qi Jun] - Experiment Setup & Performance Evaluation  
[Ong Hong Liang] - Model Optimization and Hyperparameter Tuning  

## 📜 License
This project is open-source and available under the MIT License.