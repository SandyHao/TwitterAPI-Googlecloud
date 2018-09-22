import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

#set font
font = ImageFont.truetype("C:\Windows\Fonts\Arial.ttf", 24)

#for i in rang(1,51)
imageFile = "%03d.jpg"
im1 = Image.open(imageFile)

#add label on pictures
draw = ImageDraw.Draw(im1)
draw.text((160, 0), label......., (255, 0, 0), font=font)    #label is the one get from google cloud vision api
draw = ImageDraw.Draw(im1)                          #draw

#save as
im1.save('%03d.jpg'%(i))