
from __future__ import print_function
import statistics
from PIL import Image

theImages = []

# path for my Windows machine. You will need to change this.
imagePath = "C:\\Users\\Mohamed\\Desktop\\Project1Images\\"

picv1= Image.open(imagePath + "1.png")
picv1 = Image.open(imagePath + "1.png")
picv1.load()
picv2= Image.open(imagePath + "2.png")
picv2 = Image.open(imagePath + "2.png")
picv2.load()
picv3= Image.open(imagePath + "3.png")
picv3 = Image.open(imagePath + "3.png")
picv3.load()
picv4= Image.open(imagePath + "4.png")
picv4 = Image.open(imagePath + "4.png")
picv4.load()
picv5= Image.open(imagePath + "5.png")
picv5 = Image.open(imagePath + "5.png")
picv5.load()
picv6= Image.open(imagePath + "6.png")
picv6=Image.open(imagePath + "6.png")
picv6.load()
picv7= Image.open(imagePath + "7.png")
picv7 = Image.open(imagePath + "7.png")
picv7.load()
picv8= Image.open(imagePath + "8.png")
picv8 = Image.open(imagePath + "8.png")
picv8.load()
picv9= Image.open(imagePath + "9.png")
picv9 = Image.open(imagePath + "9.png")
picv9.load()


pictureWidth=495
pictureHeight=557
arrayImages=[picv1,picv2,picv3,picv4,picv5,picv6,picv7,picv8,picv9]
finalImage=Image.new("RGB",(pictureWidth,pictureHeight))
finalImagePixelAccess=finalImage.load()
#finalImage.show()
#for loops the itarates through the pixels in each photo
for x in range (0,pictureWidth):
    for y in range(0,pictureHeight):
        redPixelList=[]
        greenPixelList=[]
        bluePixelList=[]
        for myImage in arrayImages:


            myRed, myGreen,myBlue=myImage.getpixel((x,y))
            redPixelList.append(myRed)
            greenPixelList.append(myGreen)
            bluePixelList.append(myBlue)
            #putting the median pixels in the picture file
        medianRed=int(statistics.median(redPixelList))
        medianGreen=int(statistics.median(greenPixelList))
        medianBlue=int(statistics.median(bluePixelList))

        finalImagePixelAccess[x,y]=(medianRed,medianGreen,medianBlue)





finalImage.show()




    






