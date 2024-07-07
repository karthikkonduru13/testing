from flask import Flask, request,jsonify
from configuration.cors_headers import add_cors_headers
from configuration.db_connection import get_database_connection
from function_view_user import function_view_user
from function_get_users import function_get_users

import os
app = Flask(__name__)

@app.route('/insert', methods=['POST','OPTIONS'])
def insert_data():

    if request.method == 'POST':
        # Get the JSON data from the request
        json_data = request.form['json']

        # Save the PDF file
        if 'image1' in request.files:
            pdf_file = request.files['image1']
#            pdf_file.save(os.path.join('uploads', pdf_file.filename))
#            print(pdf_file)
            file_data = pdf_file.read()

            mydb = get_database_connection()
            sql = "INSERT INTO temp1 (LastName, FirstName, aadharm) VALUES (%s, %s,%s)"
            val = ("last_name_localhost", "first_name_localhost", file_data)

            mycursor = mydb.cursor()
            mycursor.execute(sql, val)
            mydb.commit()


        response = jsonify({'message': 'theOutput'})
        return add_cors_headers(response)
    elif request.method == 'OPTIONS':
        response = jsonify({'message': 'theOutput'})
        return add_cors_headers(response)


@app.route('/users', methods=['GET'])
def get_users():
    try:
        response = function_get_users()
        return add_cors_headers(response), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/view_user', methods=['GET'])
def view_user():
    user_id = request.args.get('id')
    user_dict = function_view_user(user_id)

    response = jsonify(user_dict)
    return add_cors_headers(response), 200

if __name__ == '__main__':
    app.run(debug=True)
