"Now we will build gui"

from tkinter import *
from PIL import ImageTk,Image
from editFunctions import satPic, brightPic, sharpenPic, blurPic, rotateCounter, rotateClock, cropPic, sketchPic, oilPic, pencilPic, foilPic, negativePic
#change image on the panel using counter function 
def changeImage(counter):
     img = ImageTk.PhotoImage(Image.open('image' + str(counter) + '.jpg'))
     panel.configure(image=img)
     panel.image = img

#functions and filters
#increasing the counter by 1 ans saving the image 
#simultaneously changing the picture on panel
def sharpenImgFunc():
     global counter
     curImg = 'image' + str(counter) + '.jpg'
     counter = counter + 1
     sharpenPic(curImg, counter)
     changeImage(counter)
def BrightFunc():
     global counter
     curImg = 'image' + str(counter) + '.jpg'
     counter = counter + 1
     brightPic(curImg, counter)
     changeImage(counter)
def satFunc():
     global counter
     curImg = 'image' + str(counter) + '.jpg'
     counter = counter + 1
     satPic(curImg, counter)
     changeImage(counter)

def blurImgFunc():
     global counter
     curImg = 'image' + str(counter) + '.jpg'
     counter = counter + 1
     blurPic(curImg, counter)
     changeImage(counter)
def rotateCounterFunc():
     global counter
     curImg = 'image' + str(counter) + '.jpg'
     counter = counter + 1
     rotateCounter(curImg, counter)
     changeImage(counter)
def rotateClockFunc():
     global counter
     curImg = 'image' + str(counter) + '.jpg'
     counter = counter + 1
     rotateClock(curImg, counter)
     changeImage(counter)
def cropImgFunc():
     global counter
     curImg = 'image' + str(counter) + '.jpg'
     counter = counter + 1
     cropPic(curImg, counter)
     changeImage(counter)
#undo button
def undoFunc():
     global counter
     if counter > 0:
          counter = counter - 1
     changeImage(counter)
def sketchImgFunc():
     global counter
     curImg = 'image' + str(counter) + '.jpg'
     counter = counter + 1
     sketchPic(curImg, counter)
     changeImage(counter)
def oilImgFunc():
     global counter
     curImg = 'image' + str(counter) + '.jpg'
     counter = counter + 1
     oilPic(curImg, counter)
     changeImage(counter)
def paintImgFunc():
     global counter
     curImg = 'image' + str(counter) + '.jpg'
     counter = counter + 1
     pencilPic(curImg, counter)
     changeImage(counter)
def foilImgFunc():
     global counter
     curImg = 'image' + str(counter) + '.jpg'
     counter = counter + 1
     foilPic(curImg, counter)
     changeImage(counter)
def negativeImgFunc():
     global counter
     curImg = 'image' + str(counter) + '.jpg'
     counter = counter + 1
     negativePic(curImg, counter)
     changeImage(counter)
def negativeImgFunc():
     global counter
     curImg = 'image' + str(counter) + '.jpg'
     counter = counter + 1
     negativePic(curImg, counter)
     changeImage(counter)
def enhanceImgFunc():
     global counter
     curImg = 'image' + str(counter) + '.jpg'
     counter = counter + 1
     brightPic(curImg, counter)
     satPic(curImg, counter)
     
     changeImage(counter)
#return original
def Original():
     global counter
     
     counter = 0
     
     changeImage(counter)

    
     
     
#resizing the image to fit in frame
imo=Image.open("DSC_0658.JPG")
basewidth = min(600,int(imo.size[0]/1.3))
wpercent = (basewidth/float(imo.size[0]))
hsize = int((float(imo.size[1])*float(wpercent)))
imo = imo.resize((basewidth,hsize), Image.Resampling.LANCZOS)
imo.save('image0.jpg')


#tinker 
main = Tk()
counter = 0

main.title("Photo Editor")
main.geometry("1050x650")
var = IntVar()
editingBox = Frame(main)

undoButton = Button(main, text="Undo", command=undoFunc, font=15)
undoButton.pack(side=BOTTOM, pady=15)

formatLabel = Label(editingBox, text = "Format", font=15)
formatLabel.pack(side = TOP, pady=10)
SharpenButton = Button(editingBox, text="Sharpen Image", command=sharpenImgFunc, width=15)
SharpenButton.pack(side = TOP)
BlurButton = Button(editingBox, text="Blur Image", command=blurImgFunc, width=15)
BlurButton.pack(side = TOP)
CropButton = Button(editingBox, text="Crop", command=cropImgFunc, width=15)
CropButton.pack(side = TOP)
rotateCounterButton = Button(editingBox, text="Rotate anticlockwise", command = rotateCounterFunc, width=15)
rotateCounterButton.pack(side = TOP)
rotateClockButton = Button(editingBox, text="Rotate Clockwise", command = rotateClockFunc, width=15)
rotateClockButton.pack(side = TOP)
brightButton = Button(editingBox, text="Brightness", command=satFunc, width=15)
brightButton.pack(side = TOP)
originalButton = Button(editingBox, text="Original", command=Original, width=15)
originalButton.pack(side = TOP)
satButton = Button(editingBox, text="Saturation", command=satFunc, width=15)
satButton.pack(side = TOP)



img = ImageTk.PhotoImage(Image.open('image0.jpg'))


panel = Label(main, image=img)
panel.pack(side=LEFT, padx=6)
negativeButton = Button(editingBox, text="Photo negative", command=negativeImgFunc, width=15)
negativeButton.pack(side = BOTTOM)


foilButton = Button(editingBox, text="Foil art", command=foilImgFunc, width=15)
foilButton.pack(side = BOTTOM)
pencilButton = Button(editingBox, text="Sharp paint", command=paintImgFunc, width=15)
pencilButton.pack(side = BOTTOM)
oilButton = Button(editingBox, text="Oil paint", command=oilImgFunc, width=15)
oilButton.pack(side = BOTTOM)
sketchButton = Button(editingBox, text="Sketch light", command=sketchImgFunc, width=15)
sketchButton.pack(side = BOTTOM)
enhanceButton = Button(editingBox, text="Enhance", command=enhanceImgFunc, width=15)
enhanceButton.pack(side = BOTTOM)
filterLabel = Label(editingBox, text = "Filters", font=16)
filterLabel.pack(side = BOTTOM, pady=3)

editingBox.pack()
main.mainloop()