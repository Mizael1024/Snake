from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from audio_converter import AudioFile
from database import Database

app = Flask(__name__)
db = Database()

@app.route('/convert', methods=['POST'])
def convert_audio_to_text():
    if 'audio_file' not in request.files:
        return jsonify({'error': 'No audio file provided'}), 400

    file = request.files['audio_file']
    filename = secure_filename(file.filename)
    file_path = f"uploads/{filename}"
    file.save(file_path)

    audio_file = AudioFile(file_path, file.mimetype)
    audio_file.convert_to_text()
    db.save_conversion(audio_file)

    return jsonify({'text': audio_file.text}), 200

@app.route('/history', methods=['GET'])
def get_previous_conversions():
    conversions = db.get_previous_conversions()
    return jsonify([{'file_path': c.file_path, 'format': c.format, 'text': c.text} for c in conversions]), 200

@app.route('/')
def home():
    return '''
        <h1>Audio to Text Converter</h1>
        <p>Welcome to the Audio to Text Converter. Use the /convert endpoint to convert audio files to text and the /history endpoint to view previous conversions.</p>
    '''

if __name__ == '__main__':
    app.run(debug=True)
