from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_template():
    return render_template("index.html")

@app.route("/emotionDetector")
def emot_detector():
    text_to_analyze = request.args.get("textToAnalyze")
    emotion = emotion_detector(text_to_analyze)
    return f"For the given statement, the system response is 'anger': {emotion['anger']}, 'disgust': {emotion['disgust']}, 'fear': {emotion['fear']}, 'joy': {emotion['joy']} and 'sadness': {emotion['sadness']}. The dominant emotion is {emotion['dominant_emotion']}"

app.run(host="0.0.0.0", port=5000)