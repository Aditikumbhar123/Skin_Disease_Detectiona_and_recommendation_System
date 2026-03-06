from flask import Flask,render_template,request
import os

from prediction import predict_disease
from severity import get_severity
from recommendation import get_recommendations
from rag_chatbot import load_rag

app = Flask(__name__, static_folder="../static", static_url_path="/static")

UPLOAD_FOLDER = "../static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

qa = load_rag()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    file = request.files["image"]

    path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(path)

    disease, confidence = predict_disease(path)

    severity = get_severity(confidence)

    rec = get_recommendations(disease)

    return render_template(
        "result.html",
        disease=disease,
        confidence=round(confidence*100,2),
        severity=severity,
        rec=rec
    )


@app.route("/chat", methods=["POST"])
def chat():

    question = request.form["question"]

    answer = qa.run(question)

    return render_template("chat.html",answer=answer)


if __name__ == "__main__":
    app.run(debug=True)