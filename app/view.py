# app/view.py

from flask import Flask, render_template, request
from app.controller import ChatController

app = Flask(__name__)
chat_controller = ChatController()

@app.route('/')
def home():
    return render_template('index.html')  # Make sure 'index.html' is in the 'templates' folder

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['user_input']
    response = chat_controller.handle_user_input(user_input)
    return render_template('index.html', user_input=user_input)
