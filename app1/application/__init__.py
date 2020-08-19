from flask import Flask
import requests
import os

app = Flask(__name__)

api = 'http://localhost:5001'
from application import routes
