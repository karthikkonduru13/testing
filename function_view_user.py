from flask import Flask, request,jsonify
from configuration.db_connection import get_database_connection

def function_view_user(user_id):

    connection = get_database_connection()

    cursor = connection.cursor()
    query = "SELECT * FROM user WHERE id = %s"
    cursor.execute(query, (user_id,))
    user_data = cursor.fetchone()

    connection.close()
    user_dict = {
    'id': user_data[0],
    'LastName': user_data[1],
    'FirstName': user_data[2],
    'UserName': user_data[3]
    }
    return user_dict


  

