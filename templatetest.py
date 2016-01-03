from PIL import Image, ImageMath, ImageChops, ImageDraw, ImageFont #ThePIL
import tkinter as tk
import uuid
import os, random, string
from tkinter import filedialog


##this is just the part that locates the meme upper left and lower right points on the main script, but without the extra parts (good for testing without making export locations)


root=tk.Tk()
root.withdraw()

imgFile=filedialog.askopenfilename()
img = Image.open(imgFile)
width, height = img.size
pixels = img.load()
data = []
cpixel = pixels[0, 0]
data.append(cpixel)
memecount=data[0][1]
memecount=memecount-1
print(str(memecount) + " memes located")
for meme in range(memecount):
    meme=meme+1
    print(meme)
    pixels = img.load()
    data = []
    for c in range(1):
        for v in range(height):
            cpixel = pixels[c, v]
            data.append(cpixel)
            colour2 = (data[v][0], data[v][1], data[v][2])
            if colour2 == (meme, 255, 255):
                print("y found!")
                pixle_location_height=v;
    pixels = img.load()
    data = []
    height1 = 0
    width1 = 0
    for x in range(width):
        for y in range(1):
            cpixel = pixels[x, y]
            data.append(cpixel)
            colour = (data[x][0], data[x][1], data[x][2])
            if colour == (meme, 255, 255):
                print("x found!")
                pixle_location_width=x;
    img = Image.open(imgFile)
    pixels = img.load()
    data = []
    for j in range(1):
        for k in range(height):
            cpixel = pixels[j, k]
            data.append(cpixel)
            colour3 = (data[k][0], data[k][1], data[k][2])
            if colour3 == (255, meme, 255):
                print("y end found!")
                pixle_location_end_height=k;
    pixels = img.load()
    data = []
    for u in range(width):
        for i in range(1):
            cpixel = pixels[u, i]
            data.append(cpixel)
            colour4 = (data[u][0], data[u][1], data[u][2])
            if colour4 == (255, meme, 255):
                print("x end found!")
                pixle_location_end_width=u;
    print("meme " + str(meme) + " location is: ", (pixle_location_height, pixle_location_width));
    memeresx=int(pixle_location_end_width)
    memeresy=int(pixle_location_end_height)
    memeresend=(memeresx-pixle_location_width),(memeresy-pixle_location_height)
    print("meme " + str(meme) + " resolution is: ", memeresend)
