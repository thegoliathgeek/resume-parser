
#########################
#Example Usage: 

# import requests

# url = 'http://localhost:5000/process-pdf'
# files = {'file': open('example.pdf', 'rb')}
# response = requests.post(url, files=files)
# print(response.json())


#################

# This function handles a POST request to the /process-pdf endpoint, processes an uploaded PDF file, extracts its text, and returns the text as a JSON response.

from flask import Flask, request, jsonify
# import fitz  # PyMuPDF
import pymupdf as fitz
import os
# from dotenv import load_dotenv
import json

static_dir = os.path.join(os.getcwd(), 'static')
if not os.path.exists(static_dir):
    os.makedirs(static_dir)

# load_dotenv()

app = Flask(__name__)

@app.route('/process-pdf', methods=['POST'])
def process_pdf():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    try:
        pdf_text = ""
        with fitz.open(stream=file.stream.read(), filetype="pdf") as pdf:
            for page in pdf:
                pdf_text += page.get_text()

        return jsonify({"pdf_text": pdf_text}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='', port=5000, debug=True)
