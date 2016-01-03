import os, random, string #import some important stuff
import tkinter as tk #ui shit
import uuid #ruining file names every day
from PIL import Image, ImageMath, ImageChops, ImageDraw, ImageFont #imports shitty image editing library
from tkinter import filedialog #more ui shit
root=tk.Tk() #loads the hardcore heavy 100000years on paint ui
root.withdraw() #draws the "ui"
memecount=0
print("where do you want your memes to go?") #robots are your friends
exportpath=filedialog.askdirectory() #defines the export location
print("you do have templates right?") #smug robot likes you
templatefilepath=filedialog.askdirectory() #defines the template location
print("like autistic kid with a dakimakura paradies ghetto memes on facebook for more (tell me where your memes are)") #www.facebook.com/autsimomeme/
memefilepath=filedialog.askdirectory() #defines the meme location
filename=input("what would you like the memes to be called? (im going to make it random anyway) ") #this is a real friendly robot
countx=input("how many memes do you want? ") #thats the question we have all been waiting for
countx=int(countx) #lots of memes
count = 0 #the real final countdown
while (count < countx): 
    filename="" #fixes that thing where it makes the name too long
    templatefile=random.choice(os.listdir(templatefilepath)) #choses random template
    meme1file=random.choice(os.listdir(memefilepath)) #choses random meme
    template=Image.open(templatefilepath+"/"+templatefile).convert('RGBA') #imports template 
    new_template=Image.new('RGBA',template.size) #makes an empty image
    new_template.paste(template, (0,0)) #places template on the blank image
    img = Image.open(templatefilepath+"/"+templatefile) #prepares for pixel reading
    width, height = img.size #get the dimensions as variables
    pixels = img.load()
    data = []
    cpixel = pixels[0, 0]
    data.append(cpixel)
    memecount=data[0][1]
    memecount=memecount-1
#    if memecount <= 100:     
#        print(str(memecount))
    for meme2 in range(memecount):
        meme2=meme2+1
        meme1file=random.choice(os.listdir(memefilepath))
        meme=Image.open(memefilepath+"/"+meme1file).convert('RGBA') #loads the meme
        pixels = img.load() #loads the pixels in the template
        data = [] #loads data
        for c in range(1): #1 pixel down
            for v in range(height): #does the following on each pixel on the top
                cpixel=pixels[c, v] #arranges the coordinates to be readable
                data.append(cpixel) #prepares to get rgb info for the pixel
                colour2=(data[v][0], data[v][1], data[v][2]) #loads the r, g and b info for the pixel
                if colour2 == (meme2, 255, 255): #if the rgb matches that of the memelocation colour it saves the y location
                    pixle_location_height=v; 
                if colour2 == (255, meme2, 255): #if the rgb matches that of the memesize colour it saves the y location
                    pixle_location_end_height=v;  
        pixels = img.load() #reloads the pixels in the template
        data = [] #reloads data
        for x in range(width): #does the following on each pixel on the top
            for y in range(1): #1 pixel across
                cpixel=pixels[x, y] #arranges the coordinates to be readable
                data.append(cpixel) #prepares to get rgb info for the pixel
                colour=(data[x][0], data[x][1], data[x][2]) #loads the r, g and b info for the pixel
                if colour == (meme2, 255, 255): #if the rgb matches that of the memelocation colour it saves the x location
                    pixle_location_width=x;
                if colour == (255, meme2, 255): #if the rgb matches that of the memesize colour it saves the x location
                    pixle_location_end_width=x
        memesize1=int((pixle_location_end_width)-(pixle_location_width)) #prepares the scaling of the meme
        memesize2=int((pixle_location_end_height)-(pixle_location_height))
        meme=meme.resize((memesize1, memesize2)) #makes meme 1 a set size (just the right size)
        memelocation1=int(pixle_location_width) #sets the location for future use
        memelocation2=int(pixle_location_height)
        new_template.paste(meme,(memelocation1, memelocation2))#places meme 1 on a location on the template image (now the right place)
#        if memecount <= 100: #turns out prints make it take way longer, so with bulk generating it wont take so long
        print("meme " +str(meme2)+ " has been pasted at: ", memelocation1, ",", memelocation2)
#    watermarkdraw=Image.new('RGBA', template.size, (255,255,255,0)) #makes a blank image for the watermark
#    watermark=ImageDraw.Draw(watermarkdraw) #something to get ready to make the water mark real (im sure its not necessary)
#    draw=ImageDraw.Draw(watermarkdraw) #making a second variable of the same thing for no reason?
#    watermarklocation1=memelocation1
#    watermarklocation2=memelocation2
#    draw.text((watermarklocation1,watermarklocation2),"www.facebook.com/autsimomeme/",fill=(255,255,255,100)) #writes stuff on the watermark
#    new_template=Image.alpha_composite(new_template, watermarkdraw) #merges the watermark onto the image
    filenameruiner=str(uuid.uuid4()) #prepares for some random shit
    filename=filename+filenameruiner #adds some random shit to the end of the file name
    os.chdir(exportpath) #prepares export path
    new_template.save(filename + ".bmp") #saves the file
#    if memecount <= 100: #turns out prints make it take way longer, so with bulk generating it wont take so long
#        print(new_template) #so you can see the memes are real
    count=count+1;
print("your memes are done") #well done

