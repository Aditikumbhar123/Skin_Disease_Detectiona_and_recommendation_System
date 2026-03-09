# AI Skin Disease Detection & Dermatology Assistant

An AI-powered dermatology support system that performs **skin disease classification from images** and provides **AI-driven medical guidance using Retrieval-Augmented Generation (RAG)**.
The system integrates **Deep Learning, Computer Vision, and Large Language Models** to assist users in identifying potential skin conditions and receiving dermatology recommendations.

---

## Project Overview

Skin diseases are among the most common health issues worldwide, and early identification can help in timely treatment. This project builds an **intelligent dermatology assistant** that uses **machine learning and AI-powered knowledge retrieval** to analyze skin images and answer dermatology-related queries.

The system enables users to upload images of skin conditions, receive predicted disease classifications, assess severity levels, and interact with an AI chatbot for dermatology guidance.

---

## Key Features

### Skin Disease Detection

* Upload an image of a skin condition
* CNN-based deep learning model predicts the disease class

### Severity Analysis

* Evaluates the severity level of the detected disease
* Helps determine whether medical attention may be required

### Dermatology Recommendation System

* Provides treatment suggestions and precautionary advice
* Suggests skincare practices and possible medications

### AI Dermatology Chatbot

* Uses **Retrieval-Augmented Generation (RAG)** architecture
* Retrieves information from a dermatology knowledge base
* Answers user queries related to skin conditions

### Interactive Web Interface

* Simple web interface for uploading images
* Displays prediction results and chatbot responses

---

## System Architecture

User Uploads Image
↓
Image Preprocessing
↓
CNN Skin Disease Detection Model
↓
Prediction Result
↓
Severity Analysis + Recommendation Engine
↓
RAG-based Dermatology Chatbot

---

## Tech Stack

### Machine Learning & AI

* Python
* TensorFlow / Keras
* Convolutional Neural Networks (CNN)
* Computer Vision
* Retrieval-Augmented Generation (RAG)

### Backend

* Flask
* Python APIs

### Frontend

* HTML
* CSS
* JavaScript

### Data Processing

* NumPy
* Pandas
* Image preprocessing techniques

### Knowledge Retrieval

* Text embeddings
* Semantic search
* Vector-based document retrieval

---

## Project Structure

```
Skin_Disease_Detection
│
├── backend
│   ├── app.py
│   ├── prediction.py
│   ├── recommendation.py
│   ├── severity.py
│   ├── rag_chatbot.py
│   └── templates
│
├── knowledge_base
│   └── dermatology_docs.txt
│
├── models
│   └── skin disease model files
│
├── static
│   ├── css
│   └── uploads
│
├── .gitignore
└── README.md
```

---

## Installation

Clone the repository

```
git clone https://github.com/Aditikumbhar123/Skin_Disease_Detectiona_and_recommendation_System.git
```

Navigate to the project directory

```
cd Skin_Disease_Detection
```

Create a virtual environment

```
python -m venv venv
```

Activate the environment (Windows)

```
venv\Scripts\activate
```

Install dependencies

```
pip install -r requirements.txt
```

---

## Running the Application

Start the Flask server

```
python backend/app.py
```

Open your browser and visit

```
http://127.0.0.1:5000
```

---

## Future Improvements

* Deploy the application using **Docker and cloud platforms**
* Improve model accuracy using **larger dermatology datasets**
* Add **mobile-based skin disease detection**
* Integrate **advanced LLM-based medical reasoning**
* Expand the dermatology knowledge base

---

