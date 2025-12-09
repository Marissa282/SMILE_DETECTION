# SMILE_DETECTION
A comparative study of three approaches to smile detection—CNN, Autoencoder, and SVM + PCA—evaluated on the same LFW subset. The CNN achieved the highest accuracy, the SVM offered the best efficiency, and the Autoencoder underperformed for this task.

# Smile Detection: CNN vs Autoencoder vs SVM

This project compares three different approaches to **smile detection** using a curated subset of the LFW dataset: a **Convolutional Neural Network (CNN)**, a **Convolutional Autoencoder** trained as a one-class anomaly detector, and a **Support Vector Machine (SVM) with PCA**. All models were trained using the same preprocessing steps, stratified splits, and fixed random seed to ensure a fair comparison.

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

