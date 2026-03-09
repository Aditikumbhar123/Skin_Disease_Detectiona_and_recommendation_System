import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Load the trained model
model = load_model("skin_disease_model3.keras")

# Class names (based on your folders)
class_names = ['acne', 'eczema', 'psoriasis']

# GUI prediction function
def predict_image(img_path):
    # Load and preprocess the image to match model input
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = img_array / 255.0  # Normalization: match training!
    img_array = np.expand_dims(img_array, axis=0)

    # Get prediction
    predictions = model.predict(img_array)
    predicted_index = np.argmax(predictions)
    predicted_class = class_names[predicted_index]
    confidence = round(100 * np.max(predictions), 2)

    # Show detailed output (optional)
    print("\n📊 Prediction Probabilities:")
    for i, class_name in enumerate(class_names):
        print(f"{class_name}: {predictions[0][i]*100:.2f}%")

    return predicted_class, confidence

# GUI image upload
def upload_and_predict():
    file_path = filedialog.askopenfilename()
    if file_path:
        # Display image
        img = Image.open(file_path).resize((250, 250))
        img_tk = ImageTk.PhotoImage(img)
        image_panel.config(image=img_tk)
        image_panel.image = img_tk

        # Predict and show result
        label_pred.config(text="Classifying...")
        predicted_class, confidence = predict_image(file_path)
        label_pred.config(text=f"Prediction: {predicted_class.capitalize()} ({confidence}%)")

# GUI setup
window = tk.Tk()
window.title("Skin Disease Classifier")
window.geometry("450x500")

btn_upload = tk.Button(window, text="Upload Skin Image", command=upload_and_predict, font=("Arial", 12))
btn_upload.pack(pady=20)

image_panel = tk.Label(window)
image_panel.pack()

label_pred = tk.Label(window, text="", font=("Arial", 14))
label_pred.pack(pady=20)

window.mainloop()
