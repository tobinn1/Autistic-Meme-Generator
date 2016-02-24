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
#from main import Generate

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
  exportpath=r".\templates"
  templatefilepath=r"\Random_Meme_Generator\Templates"
  memefilepath=r"\Random_Meme_Generator\Memes"
  countx=1
  countx=int(countx)
  count=0
  filename=""
  templatefile=random.choice(os.listdir(templatefilepath))
  meme1file=random.choice(os.listdir(memefilepath))
  template=Image.open(templatefilepath+"/"+templatefile).convert('RGBA') 
  new_template=Image.new('RGBA',template.size)
  new_template.paste(template, (0,0))
  img = Image.open(templatefilepath+"/"+templatefile)
  width, height = img.size
  pixels = img.load()
  data = []
  cpixel = pixels[0, 0]
  data.append(cpixel)
  memecount=data[0][1]
  memecount=memecount-1
  for meme2 in range(memecount):
      meme2=meme2+1
      meme1file=random.choice(os.listdir(memefilepath))
      meme=Image.open(memefilepath+"/"+meme1file).convert('RGBA')
      pixels = img.load()
      data = []
      for c in range(1):
          for v in range(height):
              cpixel=pixels[c, v]
              data.append(cpixel)
              colour2=(data[v][0], data[v][1], data[v][2])
              if colour2 == (meme2, 255, 255):
                  pixle_location_height=v; 
              if colour2 == (255, meme2, 255):
                  pixle_location_end_height=v;  
      pixels = img.load()
      data = []
      for x in range(width):
          for y in range(1): 
              cpixel=pixels[x, y]
              data.append(cpixel)
              colour=(data[x][0], data[x][1], data[x][2])
              if colour == (meme2, 255, 255):
                  pixle_location_width=x;
              if colour == (255, meme2, 255):
                  pixle_location_end_width=x
      memesize1=int((pixle_location_end_width)-(pixle_location_width))
      memesize2=int((pixle_location_end_height)-(pixle_location_height))
      meme=meme.resize((memesize1, memesize2))
      memelocation1=int(pixle_location_width)
      memelocation2=int(pixle_location_height)
      new_template.paste(meme,(memelocation1, memelocation2))
      print("meme " +str(meme2)+ " has been pasted at: ", memelocation1, ",", memelocation2)
  watermarkdraw=Image.new('RGBA', template.size, (255,255,255,0))
  watermark=ImageDraw.Draw(watermarkdraw)
  draw=ImageDraw.Draw(watermarkdraw)
  watermarklocation1=memelocation1
  watermarklocation2=memelocation2
  draw.text((watermarklocation1,watermarklocation2),"www.facebook.com/autsimomeme/",fill=(102,0,102,100))
  new_template=Image.alpha_composite(new_template, watermarkdraw)
  filenameruiner=str(uuid.uuid4())
  filename=filename+filenameruiner
  new_template.save("temp.jpg")
#  shutil.move(("temp.bmp"), ".\templates")
  return render_template('generate.html')
if __name__ == "__main__":
  app.run(host='0.0.0.0')
