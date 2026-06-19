from flask import Flask, render_template, request from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_template("index.html")

@app.route("/emotionDetector")
request.args.get("")