from flask import Flask, render_template
import os, random, string
from PIL import Image, ImageMath, ImageChops, ImageDraw, ImageFont
from facepy import GraphAPI
import uuid
import __main__

exportpath=r".\Random_Meme_Generator\Archives"
templatefilepath=r".\Random_Meme_Generator\Templates"
memefilepath=r".\Random_Meme_Generator\Memes"
countx=1
countx=int(countx)
count=0
filename=""

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('template.html')

@app.route('/my-link/')
def my_link(): 
  Generate
  return('Meme Generated and uploaded')

if __name__ == '__main__':
  app.run(debug=True)
