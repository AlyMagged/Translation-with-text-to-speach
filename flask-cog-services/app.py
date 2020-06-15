from flask import Flask, render_template, url_for, jsonify, request
import translate, synthesize

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate-text' ,methods=['POST'])
def translate_text():
    data = request.get_json()
    text_input = data['text']
    translation_output = data['to']
#    response = translate.get_translation(text_input=text_input, language_output=translation_output)
    return jsonify(['hamada'])

@app.route('/text-to-speach', methods=['POST'])
def text_to_speach():
    data = request.get_json()
    text_input = data['text']
    voice_font = data['voice']
    tts = synthesize.TextToSpeech(text_input, voice_font)
    tts.get_token()
    audio_response = tts.save_audio()
    return audio_response