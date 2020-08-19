from flask import Flask, jsonify, render_template, url_for
import requests
from application import app



@app.route('/', methods=['GET'])
def home():
    return render_template('home.html', title='Home')

@app.route('/generate', methods=['GET','POST'])
def generate():
    response = requests.get('http://localhost:5000/animal')
    json_response = response.json()
    display = str(json_response)
    response2 = requests.post('http://localhost:5001/noise',json = json_response)
    json_response2 = response2.json()
    display2 = str(json_response2)
    
    
    return render_template('generate.html', title='Animal Noises', animal=display, noise=display2)
    

