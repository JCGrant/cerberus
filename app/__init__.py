from flask import Flask
from .door import Door

app = Flask(__name__)
door = Door(output_pin=18)

from .views import *
