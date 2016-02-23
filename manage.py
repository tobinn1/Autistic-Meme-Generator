#!/usr/bin/env python
import os
import sys
from flask import Flask, render_template
import os, random, string
from PIL import Image, ImageMath, ImageChops, ImageDraw, ImageFont
from facepy import GraphAPI
import uuid
from flask.ext.heroku import Heroku
from main import Generate

app = Flask(__name__)
heroku = Heroku(app)

@app.route("/")
def index():
  return render_template('template.html')

@app.route("/generate/")
def my_link(): 
  Generate()
  return('complete')

if __name__ == "__main__":
  app.run(host='0.0.0.0')
