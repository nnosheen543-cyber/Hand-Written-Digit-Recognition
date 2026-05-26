# Handwritten Digit Recognition

A simple Handwritten Digit Recognition application built using Python, Scikit-learn, Tkinter, and PIL.  
This project allows users to draw digits (0–9) on a canvas and predicts the digit using a trained Machine Learning model.

## Features
1. Draw digits on a GUI canvas
2. Predict handwritten numbers instantly
3. Machine Learning model using SVM (Support Vector Machine)
4. Confidence percentage display
5. Clear canvas functionality
6. Beginner-friendly Python project
   
## Technologies Used
1. Python
2. Scikit-learn
3. Tkinter
4. NumPy
5. Pillow (PIL)

## File Structure

```text
handwrittenDigit.py
README.md
```
## How It Works

1. The user draws a digit on the canvas.
2. The image is processed and resized to 8×8 pixels.
3. The trained SVM model predicts the digit.
4. The prediction and confidence score are displayed.

## Installation
Install the required libraries:
```bash
pip install scikit-learn pillow numpy
```
## Run the Project
```bash
python handwrittenDigit.py
```
## Dataset Used :This project uses the built-in Digits Dataset from Scikit-learn.
## Example Output
```text
Predicted: 7 (98%)
```
## Learning Concepts
This project demonstrates:
- Machine Learning basics
- GUI development with Tkinter
- Image preprocessing
- Digit classification
- SVM model training
- Event handling in Python
## Author

Your Name
