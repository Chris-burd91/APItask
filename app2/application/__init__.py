from flask import Flask
import requests
import os

app = Flask(__name__)


from app2.application import routes
