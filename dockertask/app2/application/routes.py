from flask import Flask, jsonify, Response, request
import requests
from application import app

import random


@app.route('/animal', methods=['GET'])
def animal():
    animals = ['TIGER', 'LION', 'CAT', 'DOLPHIN']
    animal = animals[random.randrange(4)]
    return jsonify({'animal':animal})


@app.route('/noise', methods=['GET','POST'])
def noise():
    animal = request.get_json()
    name = animal['animal']
    noises = {'TIGER':'Raaaaw','LION':'RAAAWW','CAT':'Meow','DOLPHIN':'Ehcechehehcheece'}   
    noise = noises[name]
    return jsonify({'noise':noise})