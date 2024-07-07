from flask import Flask, request, jsonify
from configuration.cors_headers import add_cors_headers

import base64

app = Flask(__name__)

@app.route('/viewroute', methods=['POST'])
def view_data():
    pdf_path = 'uploads/Invoice_1644649097.pdf'
    with open(pdf_path, 'rb') as pdf_file:
        encoded_pdf = base64.b64encode(pdf_file.read()).decode('utf-8')
    return add_cors_headers(jsonify({'pdf': encoded_pdf}))

if __name__ == '__main__':
    app.run(debug=True)