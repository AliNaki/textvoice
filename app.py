from flask import Flask, request, render_template
import pyttsx3

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        gender = int(request.form['gender'])
        sentence = request.form['sentence']

        text_speech = pyttsx3.init()
        text_speech.setProperty('rate', 116)
        voices = text_speech.getProperty('voices')
        text_speech.setProperty('voice', voices[gender].id)

        try:
            text_speech.say(sentence)
            text_speech.runAndWait()
        except Exception as e:
            app.logger.error(f"Error during audio playback: {str(e)}")

    return render_template('index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0")
