'''
Flask server for the Emotion Detection application.
'''

# Import Flask, render_template, request from the flask framework package
from flask import Flask, render_template, request

# Import the sentiment_analyzer function from the package created:
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    '''
    Render the home page.
    '''
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_detector_route():
    ''' 
    Receives text input, runs emotion detection,
    and returns formatted output
    '''

    # Retrive the text to analyze from the request arguments
    text_to_analyze = request.args.get("textToAnalyze")

    # Pass the text to the sentiment_analyzer function
    response = emotion_detector(text_to_analyze)

    # Extract the emotion and scores from the response
    anger = response["anger"]
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]
    dominant_emotion = response["dominant_emotion"]

    # Incorporate error handling when dominant emotion is None
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    # Return formatted response
    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
