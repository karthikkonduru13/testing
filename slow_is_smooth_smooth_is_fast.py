from flask import Flask, request,jsonify
from configuration.cors_headers import add_cors_headers
from configuration.db_connection import get_database_connection
import os, json
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/view', methods=['POST','OPTIONS'])
def view_data():

    if request.method == 'POST':
      # Get the JSON data from the request
      json_data = request.form['json']
      data = json.loads(json_data)
      print(json_data)
      varFirstName = data.get('varFirstName')
      varLastName = data.get('varLastName')
      varAddressProof = data.get('varAddressProof')

      if 'image1' in request.files:
        pdf_file = request.files['image1']
        pdf_file.save(os.path.join('uploads', pdf_file.filename))
        print(pdf_file)

        varImageFileName = pdf_file.filename

        mydb = get_database_connection()
        sql = "INSERT INTO temp1 (FirstName, LastName, address_proof, image_file_name ) VALUES (%s, %s, %s, %s)"
        val = (varFirstName, varLastName, varAddressProof, varImageFileName)

        mycursor = mydb.cursor()
        mycursor.execute(sql, val)
        mydb.commit()

        response = jsonify({'message': 'theOutput'})
        return add_cors_headers(response)
    elif request.method == 'OPTIONS':
        response = jsonify({'message': 'theOutput'})
        return add_cors_headers(response)

@app.route('/upload', methods=['POST','OPTIONS'])
def upload_data():

    if request.method == 'POST':
      # Get the JSON data from the request
      json_data = request.form['json']
      data = json.loads(json_data)
      print(json_data)
      varFirstName = data.get('varFirstName')
      varLastName = data.get('varLastName')
      varAddressProof = data.get('varAddressProof')

      if 'image1' in request.files:
        pdf_file = request.files['image1']
        pdf_file.save(os.path.join('uploads', pdf_file.filename))
        print(pdf_file)

        varImageFileName = pdf_file.filename

        mydb = get_database_connection()
        sql = "INSERT INTO temp1 (FirstName, LastName, address_proof, image_file_name ) VALUES (%s, %s, %s, %s)"
        val = (varFirstName, varLastName, varAddressProof, varImageFileName)

        mycursor = mydb.cursor()
        mycursor.execute(sql, val)
        mydb.commit()

        response = jsonify({'message': 'theOutput'})
        return add_cors_headers(response)
    elif request.method == 'OPTIONS':
        response = jsonify({'message': 'theOutput'})
        return add_cors_headers(response)

if __name__ == '__main__':
    app.run(debug=True)
