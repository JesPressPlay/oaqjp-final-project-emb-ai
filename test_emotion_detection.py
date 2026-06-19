import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotions(self):
        result_1 = emotion_detector("I am glad this happened") self.assertEqual(result_1["dominant_emotion" = "joy"])
        result_2 = emotion_detector("I am really mad about this")
        result_3 = emotion_detector("I feel disgusted just hearing abou this")
        result_4 = ""

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self): # Test case for positive sentiment
    result_1 = sentiment_analyzer('I love working with Python') self.assertEqual(result_1['label'], 'SENT_POSITIVE') # Test case for negative sentiment
    result_2 = sentiment_analyzer('I hate working with Python') self.assertEqual(result_2['label'], 'SENT_NEGATIVE') # Test case for neutral sentiment
    result_3 = sentiment_analyzer('I am neutral on Python') self.assertEqual(result_3['label'], 'SENT_NEUTRAL')