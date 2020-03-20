from flask import Flask, render_template, request, jsonify, flash, redirect, session, abort
from werkzeug import secure_filename
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms.fields import DateField
import os
import pandas as pd
import math
import shutil
import sys
from datetime import timedelta
from cryptography.fernet import Fernet
from pymysql import connect
from datetime import datetime
import json

app = Flask(__name__)

@app.route('/')
def home():
   return 'Hello world'

if __name__ == '__main__':
   app.run()