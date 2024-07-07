from flask import Flask, request, jsonify, Response #type: ignore
from components.registration import register_user_sql
import json, os

app = Flask(__name__)

@app.route('/register_user_route1', methods=['POST','OPTIONS'])
def register_user_app_function():
    if request.method == 'POST':
        data = request.json

        FirstName = data.get('varFirstName')

        return FirstName
