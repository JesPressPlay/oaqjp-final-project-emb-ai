""" Flask server that serves the emotion detection web app."""
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_template():
    """Renders the index page."""
    return render_template("index.html")

@app.route("/emotionDetector")
def emot_detector():
    """Runs emotion detection on the submitted text and returns the formatted response."""
    text_to_analyze = request.args.get("textToAnalyze")
    emotion = emotion_detector(text_to_analyze)

    # Check the dominant emotion
    if emotion['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    return (
        f"For the given statement, the system response is 'anger': {emotion['anger']}, "
        f"'disgust': {emotion['disgust']}, 'fear': {emotion['fear']}, "
        f"'joy': {emotion['joy']} and 'sadness': {emotion['sadness']}. "
        f"The dominant emotion is {emotion['dominant_emotion']}"
        )

app.run(host="0.0.0.0", port=5000)
