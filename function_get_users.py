from flask import Flask, request,jsonify
from configuration.db_connection import get_database_connection

def function_get_users():
      connection = get_database_connection()
      cursor = connection.cursor()
      
      # Fetch all records from the 'user' table
      cursor.execute("SELECT id, LastName, FirstName, UserName FROM user")
      users = cursor.fetchall()
      
      # Convert data into JSON format
      users_json = []
      for user in users:
          user_dict = {
              'id': user[0],
              'LastName': user[1],
              'FirstName': user[2],
              'UserName': user[3]
          }

          users_json.append(user_dict)

          response = jsonify(users_json)
      return response
