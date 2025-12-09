# Smile Detection: CNN vs Autoencoder vs SVM

This project compares three different approaches to **smile detection** using a curated subset of the LFW dataset: a **Convolutional Neural Network (CNN)**, a **Convolutional Autoencoder** trained as a one-class anomaly detector, and a **Support Vector Machine (SVM) with PCA**. All models were trained using the same preprocessing steps, stratified splits, and fixed random seed to ensure a fair comparison.

---

## 📁 Dataset Description & Access

This dataset consists of two components:

### **1. Labels**
- Included in two text files:
  - `SMILE_list.txt`
  - `NON-SMILE_list.txt`
- Each file contains the filenames of images classified as **smile** or **non-smile**.

### **2. Image Files**
You must manually download the face images from:

🔗 **http://conradsanderson.id.au/lfwcrop/**

- Download **lfwcrop_color.zip**
- Extract the `.ppm` files
- Copy **all** extracted images into the directory:

## Key Results

### CNN
- Test Accuracy: **94.1%**
- Epochs: **13**
- Learning Rate: **1e-3**
- Overfitting prevention:
  - **Dropout (p = 0.65)**
  - **Weight Decay (1e-3)**
  - **Batch Normalization**
  - **Stratified splitting**
- Best overall accuracy.

### SVM + PCA
- Test Accuracy: **87.1%**
- PCA Components: **50**
- Fastest training and inference.
- Best efficiency–accuracy trade-off.

### Autoencoder (Anomaly Detection)
- Test Accuracy: **48.5%**
- Epochs: **20**
- Learning Rate: **0.01**
- Trained only on the Non-Smile class.
- Underperformed due to subtle, localized smile features not captured by reconstruction error.

## Summary
The **CNN** provides the highest accuracy, the **SVM** is the most efficient, and the **Autoencoder** is not suitable for detecting subtle facial expressions like smiles. This repository includes all code, experiments, and the full technical report.

The **CNN** provides the highest accuracy, the **SVM** is the most efficient, and the **Autoencoder** is not suitable for detecting subtle facial expressions like smiles. This repository includes all code, experiments, and the full technical report.


