# Draw a diagonal blue line
from cImage import *
myImWin = ImageWin("Line image", 300, 300)
bluePix = Pixel(0,0,255)
lineImage = EmptyImage(300,300)
for i in range(300):
   lineImage.setPixel(i,i,bluePix)
 
lineImage.draw(myImageWin)