from PIL import Image, ImageMath, ImageChops, ImageDraw, ImageFont
from tkinter import filedialog
import tkinter as tk
import os, random, string, uuid

root=tk.Tk()
root.withdraw()
print("where do you want your edited template to go?")
exportpath=filedialog.askdirectory()
loop = 1
while loop == 1:
    root=tk.Tk()
    root.withdraw()
    count=1
    imgFile=''
    print("choose base template")
    imgFile=filedialog.askopenfilename()
    memecount=input("How many memes will there be (max 20 for now): ")
    template=Image.open(imgFile)
    img=Image.new('RGBA',template.size)
    img.paste(template, (0,0))
    width, height = img.size
    while count <= int(memecount):
        pixels = img.load()
        data = []
        memelocationx=int(input("x axis location of the meme " + str(count) + " upper left corner: "))
        memelocationy=int(input("y axis location of the meme " + str(count) + " upper left corner: "))
        print("placing the upper left x axis pixel")
        if count == 1:
            pixels[memelocationx, 0] = (count, 255, 255) #theres a much easier way to do this, and i know how now but i cant be bothered re doing this :^)
        if count == 2:
            pixels[memelocationx, 0] = (count, 255, 255)
        if count == 3:
            pixels[memelocationx, 0] = (count, 255, 255)
        if count == 4:
            pixels[memelocationx, 0] = (count, 255, 255)
        if count == 5:
            pixels[memelocationx, 0] = (count, 255, 255)
        if count == 6:
            pixels[memelocationx, 0] = (count, 255, 255)
        if count == 7:
            pixels[memelocationx, 0] = (count, 255, 255)
        if count == 8:
            pixels[memelocationx, 0] = (count, 255, 255)
        if count == 9:
            pixels[memelocationx, 0] = (count, 255, 255)
        if count == 10:
            pixels[memelocationx, 0] = (count, 255, 255)
        if count == 11:
            pixels[memelocationx, 0] = (count, 255, 255)
        if count == 12:
            pixels[memelocationx, 0] = (count, 255, 255)
        if count == 13:
            pixels[memelocationx, 0] = (count, 255, 255)
        if count == 14:
            pixels[memelocationx, 0] = (count, 255, 255)
        if count == 15:
            pixels[memelocationx, 0] = (count, 255, 255)
        if count == 16:
            pixels[memelocationx, 0] = (count, 255, 255)
        if count == 17:
            pixels[memelocationx, 0] = (count, 255, 255)
        if count == 18:
            pixels[memelocationx, 0] = (count, 255, 255)
        if count == 19:
            pixels[memelocationx, 0] = (count, 255, 255)
        if count == 20:
            pixels[memelocationx, 0] = (count, 255, 255)
        print("placing the upper left y axis pixel")
        if count == 1:
            pixels[0, memelocationy] = (count, 255, 255)
        if count == 2:
            pixels[0, memelocationy] = (count, 255, 255)
        if count == 3:
            pixels[0, memelocationy] = (count, 255, 255)
        if count == 4:
            pixels[0, memelocationy] = (count, 255, 255)
        if count == 5:
            pixels[0, memelocationy] = (count, 255, 255)
        if count == 6:
            pixels[0, memelocationy] = (count, 255, 255)
        if count == 7:
            pixels[0, memelocationy] = (count, 255, 255)
        if count == 8:
            pixels[0, memelocationy] = (count, 255, 255)
        if count == 9:
            pixels[0, memelocationy] = (count, 255, 255)
        if count == 10:
            pixels[0, memelocationy] = (count, 255, 255)
        if count == 11:
            pixels[0, memelocationy] = (count, 255, 255)
        if count == 12:
            pixels[0, memelocationy] = (count, 255, 255)
        if count == 13:
            pixels[0, memelocationy] = (count, 255, 255)
        if count == 14:
            pixels[0, memelocationy] = (count, 255, 255)
        if count == 15:
            pixels[0, memelocationy] = (count, 255, 255)
        if count == 16:
            pixels[0, memelocationy] = (count, 255, 255)
        if count == 17:
            pixels[0, memelocationy] = (count, 255, 255)
        if count == 18:
            pixels[0, memelocationy] = (count, 255, 255)
        if count == 19:
            pixels[0, memelocationy] = (count, 255, 255)
        if count == 20:
            pixels[0, memelocationy] = (count, 255, 255)
        memelocationendx=int(input("x axis location of the meme " + str(count) + " lower right corner: "))
        memelocationendy=int(input("y axis location of the meme " + str(count) + " lower right corner: "))
        print("placing the lower right x axis pixel")
        if count == 1:
            pixels[memelocationendx, 0] = (255, count, 255)
        if count == 2:
            pixels[memelocationendx, 0] = (255, count, 255)
        if count == 3:
            pixels[memelocationendx, 0] = (255, count, 255)
        if count == 4:
            pixels[memelocationendx, 0] = (255, count, 255)
        if count == 5:
            pixels[memelocationendx, 0] = (255, count, 255)
        if count == 6:
            pixels[memelocationendx, 0] = (255, count, 255)
        if count == 7:
            pixels[memelocationendx, 0] = (255, count, 255)
        if count == 8:
            pixels[memelocationendx, 0] = (255, count, 255)
        if count == 9:
            pixels[memelocationendx, 0] = (255, count, 255)
        if count == 10:
            pixels[memelocationendx, 0] = (255, count, 255)
        if count == 11:
            pixels[memelocationendx, 0] = (255, count, 255)
        if count == 12:
            pixels[memelocationendx, 0] = (255, count, 255)
        if count == 13:
            pixels[memelocationendx, 0] = (255, count, 255)
        if count == 14:
            pixels[memelocationendx, 0] = (255, count, 255)
        if count == 15:
            pixels[memelocationendx, 0] = (255, count, 255)
        if count == 16:
            pixels[memelocationendx, 0] = (255, count, 255)
        if count == 17:
            pixels[memelocationendx, 0] = (255, count, 255)
        if count == 18:
            pixels[memelocationendx, 0] = (255, count, 255)
        if count == 19:
            pixels[memelocationendx, 0] = (255, count, 255)
        if count == 20:
            pixels[memelocationendx, 0] = (255, count, 255)
        print("placing the lower right y axis pixel")
        if count == 1:
            pixels[0, memelocationendy] = (255, count, 255)
        if count == 2:
            pixels[0, memelocationendy] = (255, count, 255)
        if count == 3:
            pixels[0, memelocationendy] = (255, count, 255)
        if count == 4:
            pixels[0, memelocationendy] = (255, count, 255)
        if count == 5:
            pixels[0, memelocationendy] = (255, count, 255)
        if count == 6:
            pixels[0, memelocationendy] = (255, count, 255)
        if count == 7:
            pixels[0, memelocationendy] = (255, count, 255)
        if count == 8:
            pixels[0, memelocationendy] = (255, count, 255)
        if count == 9:
            pixels[0, memelocationendy] = (255, count, 255)
        if count == 10:
            pixels[0, memelocationendy] = (255, count, 255)
        if count == 11:
            pixels[0, memelocationendy] = (255, count, 255)
        if count == 12:
            pixels[0, memelocationendy] = (255, count, 255)
        if count == 13:
            pixels[0, memelocationendy] = (255, count, 255)
        if count == 14:
            pixels[0, memelocationendy] = (255, count, 255)
        if count == 15:
            pixels[0, memelocationendy] = (255, count, 255)
        if count == 16:
            pixels[0, memelocationendy] = (255, count, 255)
        if count == 17:
            pixels[0, memelocationendy] = (255, count, 255)
        if count == 18:
            pixels[0, memelocationendy] = (255, count, 255)
        if count == 19:
            pixels[0, memelocationendy] = (255, count, 255)
        if count == 20:
            pixels[0, memelocationendy] = (255, count, 255)
        count=count+1;
    pixels[0, 0] = (130, count, 130)
    print(count)
    os.chdir(exportpath)
    img=img.convert('RGBA')
    filenameruiner=str(uuid.uuid4())
    filename=''
    filename=filename+filenameruiner
    name=input("export file name (no .bmp at end required i fixed it nerd cuz hashtag lazy XDDD) : ")
    img.save(name+".bmp")
    print("Template Created!")
    imgFile=''
    answer=input("would you like to continue? yes or no: ")
    if answer == "no":
        loop=0;
    
