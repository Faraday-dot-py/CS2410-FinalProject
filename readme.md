# Brain Tumor Segmentation using Machine Learning

*By Adam Webb & Han Le*

This project focuses on using a deep learning model, specifically U-Net, to segment brain tumors in MRI scans. The main goal is not to replace radiologists but to support them by reducing the time it takes to review scans and by highlighting suspicious tumor regions automatically.

---

## Overview

Brain tumor detection is challenging, and MRI interpretation is time-consuming.

We trained a U-Net segmentation model to detect tumor areas. While the model achieved high pixel accuracy, the Dice score shows that detecting small and irregular tumor shapes remains challenging.

Our goal is straightforward: build a model that automatically segments brain tumors from MRI images.

---

## Why This Matters

* Improve early tumor detection
* Reduce workload for medical professionals
* Increase consistency of diagnosis
* Support hospitals with limited radiologist resources

While AI cannot diagnose a patient alone, it can enhance human performance and reduce the chance of missing small or subtle tumors.

This system acts as a decision-support tool. It does not replace doctors. It helps doctors detect tumors faster and more consistently, and it reduces human workload, especially in hospitals with high scan volume.

---

## What is Image Segmentation?

Image segmentation is the process of dividing an image into meaningful regions.

For brain MRI, segmentation labels commonly include:

* Tumor tissue
* Healthy brain tissue
* Background regions

Unlike classification (tumor vs. no tumor), segmentation provides pixel-level localization used for diagnosis, treatment planning, and surgery guidance.

---

## Model: U-Net

U-Net is well-suited for this task because it:

* Keeps fine details important for detecting small tumors
* Handles small datasets effectively
* Performs both detection and localization

Architecture summary:

* **Encoder:** Extracts important features from the image and learns patterns like edges, shapes, and texture.
* **Decoder:** Reconstructs a full-sized segmentation mask and uses skip connections to preserve important details.

Model outputs are visualized with color coding:

* Green: true positive (correct tumor prediction)
* Blue: false negative (missed tumor)
* Red: false positive (incorrect tumor prediction)

---

## Dataset

We used the Brain Tumor Segmentation Dataset from Kaggle, which includes:

* MRI images
* Pixel-level tumor masks
* Multiple patient cases
* Diverse tumor locations and shapes

This dataset is suitable for supervised learning because the model learns from labeled examples. Dataset diversity helps produce a better model.

---

## Training Challenges & Solutions

### Challenge: Class Imbalance

Most images contain large background regions, so the model can inflate accuracy by predicting mostly background pixels. This can produce high accuracy while still failing to segment tumors well.

**Solution:** Use a combined loss function: Focal Loss + Dice Loss.

### Challenge: Learning Rate

* If the learning rate is too large, the model may never converge.
* If the learning rate is too small, the model learns too slowly.

**What we tried and the outcome:** Adjusting the learning rate using the Dice score often reduced performance, so we settled on a constant learning rate of 1e-4.

Dice score measures similarity between two images (1.00 is best).

---

## Performance

* **Accuracy:** 99.38%
* **Dice Score:** 0.7828

Prediction visualization uses:

* Green: correctly classified
* Blue: false positive (Type I error)
* Red: false negative (Type II error)

## Model Example Output
![27](https://github.com/user-attachments/assets/94b4de3d-688c-4bee-b8a4-d155b02088e3)


## MODEL SUMMARY  
```              Metric               Value  
        Architecture               U-Net  
         Input Shape           256x256x3  
        Output Shape           256x256x1  
    Total Parameters          31,037,633  
Trainable Parameters          31,037,633  
     Model Size (MB)              118.44  
      Encoder Layers                   4  
      Decoder Layers                   4  
    Feature Channels [64, 128, 256, 512]  
    Skip Connections                 Yes
```
