
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from image_caption_model import generate_caption
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(__file__), 'uploads')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        caption = generate_caption(filepath)

        return jsonify({'caption': caption})

if __name__ == '__main__':
    app.run(debug=True)
