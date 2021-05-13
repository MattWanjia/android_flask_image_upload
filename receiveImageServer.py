import werkzeug
from flask import Flask, jsonify, request, redirect

app = Flask(__name__)

@app.route('/save', methods=['GET', 'POST'])
def save_image_to_server():
    imagefile = request.files['image']
    filename = werkzeug.utils.secure_filename(imagefile.filename)
    print("\nReceived image File name : " + imagefile.filename)
    imagefile.save(filename)

    return "Subject Features saved"

app.run(host='0.0.0.0', port=5000)
