#!/usr/bin/env python
import os
import sys
from flask import Flask, render_template, send_file
import os, random, string
from PIL import Image, ImageMath, ImageChops, ImageDraw, ImageFont
from facepy import GraphAPI
import uuid
from flask.ext.heroku import Heroku
import shutil
from main import Generate



app = Flask(__name__)
heroku = Heroku(app)

@app.route("/")
def index():
  return render_template('template.html')

@app.route("/img/")
def img():
    return send_file("temp.jpg", mimetype='image/jpg')


@app.route("/generate/")
def my_link():
  Generate()
  return render_template('generate.html')
if __name__ == "__main__":
  app.run()
