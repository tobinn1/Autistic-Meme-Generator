#!/usr/bin/env python
import os
import sys
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

def index():
  return render_template('template.html')

def my_link(): 
  Generate
  return('Meme Generated and uploaded')

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Autistic-Meme-Generator.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
