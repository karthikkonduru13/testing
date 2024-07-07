from flask import Flask, request,jsonify, Response
from configuration.cors_headers import add_cors_headers
from configuration.db_connection import get_database_connection
import os, base64

app = Flask(__name__)

@app.route('/viewroute', methods=['POST','OPTIONS'])
def view_data():
    
    if request.method == 'POST':
#       Get the JSON data from the request
       image_path = os.path.join(os.getcwd(), 'uploads', '2.jpg')
       with open(image_path, 'rb') as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
       return add_cors_headers(jsonify({'image': encoded_image}))

#        pdf_path = os.path.join(os.getcwd(), 'uploads', 'Invoice_1644649097.pdf')
#        with open(pdf_path, 'rb') as pdf_file:
#            pdf_data = pdf_file.read()
#        return add_cors_headers(Response(pdf_data, mimetype='application/pdf'))

    elif request.method == 'OPTIONS':
        response = jsonify({'message': 'theOutput'})
        return add_cors_headers(response)

   
@app.route('/viewroute_db', methods=['POST','OPTIONS'])
def view_data_db():
    
    if request.method == 'POST':
        # Get the JSON data from the request
        print("1 one")

#        json_data = request.form['json']

        # Retrieve the image from the database

        mydb = get_database_connection()
        sql = "SELECT aadhar FROM temp1 WHERE id = %s"
        val = (1,)
        mycursor = mydb.cursor()
        mycursor.execute(sql, val)
        result = mycursor.fetchone()
        print("2 two")
        if result:
            image_data = result[0]  # Get the image data from the result
            encoded_image = base64.b64encode(image_data).decode('utf-8')
            response = {'image': encoded_image}
            print("3 three")
            theResponse = jsonify(response)
            return add_cors_headers(theResponse)
        
            # Write the image to the "backup" folder
#            backup_folder = "backup"
#            if not os.path.exists(backup_folder):
#                os.makedirs(backup_folder)

#            backup_file_path = os.path.join(backup_folder, "pdf_file.filename")
#            with open(backup_file_path, "wb") as backup_file:
#                backup_file.write(image_data)

 #           print(f"Image saved to: {backup_file_path}")
 #       else:
 #           print("Image not found in the database.")



    elif request.method == 'OPTIONS':
        response = jsonify({'message': 'theOutput'})
        return add_cors_headers(response)

if __name__ == '__main__':
    app.run(debug=True)
