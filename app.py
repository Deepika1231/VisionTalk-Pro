# visiontalk/app.py
from flask import Flask, render_template, request, jsonify
from caption_generator import generate_caption
from image_qa import answer_question
from voice_io import speak, transcribe
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if 'image' not in request.files:
            return render_template("index.html", error="No file part")

        image = request.files['image']
        if image.filename == '':
            return render_template("index.html", error="No selected file")

        image_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
        image.save(image_path)

        caption = generate_caption(image_path)
        speak(caption)

        return render_template("index.html", image_path=image_path, caption=caption)

    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    image_path = data['image_path']
    question = data['question']
    answer = answer_question(image_path, question)
    speak(answer)
    return jsonify({'answer': answer})

@app.route("/voice", methods=["GET"])
def voice():
    question = transcribe()
    return jsonify({'question': question})

if __name__ == "__main__":
    app.run(debug=True)
