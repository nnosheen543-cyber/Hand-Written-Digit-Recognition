from sklearn import datasets
from sklearn.svm import SVC
import numpy as np
from tkinter import *
from PIL import Image, ImageDraw, ImageOps

# Load dataset
digits = datasets.load_digits()
X, y = digits.data, digits.target

# Train model
model = SVC(gamma=0.001, probability=True)
model.fit(X, y)

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Digit Recognizer")

        self.canvas = Canvas(root, width=200, height=200, bg='white')
        self.canvas.grid(row=0, column=0, pady=2)

        self.label = Label(root, text="Draw a digit", font=("Times New Roman", 20))
        self.label.grid(row=0, column=1)

        Button(root, text="Predict", command=self.predict_digit).grid(row=1, column=1)
        Button(root, text="Clear", command=self.clear).grid(row=1, column=0)

        self.image = Image.new("L", (200, 200), "white")
        self.draw = ImageDraw.Draw(self.image)

        self.canvas.bind("<B1-Motion>", self.paint)

    def paint(self, event):
        x, y = event.x, event.y
        r = 7
        self.canvas.create_oval(x-r, y-r, x+r, y+r, fill='black')
        self.draw.ellipse([x-r, y-r, x+r, y+r], fill='black')

    def clear(self):
        self.canvas.delete("all")
        self.image = Image.new("L", (200, 200), "white")
        self.draw = ImageDraw.Draw(self.image)
        self.label.config(text="Draw a digit")

    def preprocess(self, img):
        img = ImageOps.invert(img)

        bbox = img.getbbox()
        if bbox is None:
            return None

        img = img.crop(bbox)

        # Resize directly to 8x8 (matches dataset)
        img = img.resize((8, 8), Image.Resampling.LANCZOS)

        img = np.array(img)

        # Normalize to 0–16 like sklearn digits dataset
        img = (img / 255.0) * 16
        img = np.round(img).astype(int)

        # Remove noise
        img = np.where(img > 1, img, 0)

        return img.flatten().reshape(1, -1)

    def predict_digit(self):
        img = self.preprocess(self.image)

        if img is None:
            self.label.config(text="Draw something!")
            return

        pred = model.predict(img)[0]
        prob = model.predict_proba(img)[0]
        confidence = int(np.max(prob) * 100)

        self.label.config(text=f"Predicted: {pred} ({confidence}%)")


# Run app
root = Tk()
app = App(root)
root.mainloop()