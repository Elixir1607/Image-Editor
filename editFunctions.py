from PIL import Image
import numpy as np
from PIL import ImageEnhance
from PIL import Image, ImageFilter
from PIL.ImageFilter import (
     BLUR, CONTOUR, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
     EMBOSS, FIND_EDGES, SHARPEN
)

#sharp pic function
def sharpenPic(curImg, counter):
     current = Image.open(curImg)
     newImg = current.filter(SHARPEN)
     newImg.save('image' + str(counter) + '.jpg')

#blur pic function   
def blurPic(curImg, counter):
     current = Image.open(curImg)
     newImg = current.filter(BLUR)
     newImg.save('image' + str(counter) + '.jpg')

#rotating image counter clockwise pic function
def rotateCounter(curImg, counter):
     newImg = Image.open(curImg)
     newImg.rotate(90).save('image' + str(counter) + '.jpg')
#rotating image clockwise function
def rotateClock(curImg, counter):
     newImg = Image.open(curImg)
     newImg.rotate(270).save('image' + str(counter) + '.jpg')     

#crop pic function
def cropPic(curImg, counter):
     current = Image.open(curImg)
     width, height = current.size
     left = width / 20
     top = height / 20
     right =  13*width / 20
     bottom =  13*height / 20
     newImg = current.crop((left, top, right, bottom))
     newImg.save('image' + str(counter) + '.jpg')

#sketchpic function
def sketchPic(curImg, counter):
     current = Image.open(curImg)
     newImg = current.filter(CONTOUR)
     newImg.save('image' + str(counter) + '.jpg')
#oilpic function
def oilPic(curImg, counter):
     current = Image.open(curImg)
     newImg = current.filter(EDGE_ENHANCE)
     newImg.save('image' + str(counter) + '.jpg')
     
#pencilpic function
def pencilPic(curImg, counter):
     current = Image.open(curImg)
     newImg = current.filter(EDGE_ENHANCE_MORE)
     newImg.save('image' + str(counter) + '.jpg')
     
#foilpic function
def foilPic(curImg, counter):
     current = Image.open(curImg)
     newImg = current.filter(EMBOSS)
     newImg.save('image' + str(counter) + '.jpg')

#negativepic function
def negativePic(curImg, counter):
     current = Image.open(curImg)
     newImg = current.filter(FIND_EDGES)
     newImg.save('image' + str(counter) + '.jpg')

#brightness function
def brightPic(curImg, counter):
     current = Image.open(curImg)
     curr_bri = ImageEnhance.Brightness(current)
     new_bri = 1.04
     newImg = curr_bri.enhance(new_bri)
     newImg.save('image' + str(counter) + '.jpg')

#saturation function
def satPic(curImg, counter):
     current = Image.open(curImg)
     curr_col = ImageEnhance.Color(current)
     new_col = 1.07
     newImg = curr_col.enhance(new_col)
     newImg.save('image' + str(counter) + '.jpg')
