import os, random, string, sys
from flask import Flask, render_template, send_file
from PIL import Image, ImageMath, ImageChops, ImageDraw, ImageFont
#from flask.ext.heroku import Heroku
from main import Generate

app = Flask(__name__)

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
