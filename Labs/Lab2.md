## IT 2750 - Lab 2

*Use Chapter 2 to complete this lab.*

1. Create a folder in your repository called Lab2.
2. In the Lab 1 folder add a file called README.md.
3. In your README.md file, describe - in a few sentences - what we've covered in lesson 2. 
4. Again, in README.md, answer the following questions:
5. Create a file called archimedes.py. In archimedes.py, implement the archimedes in Listings 2.2 and 2.4 in the chapter. 
```
import math  

def archimedes(numsides):  
    innerangleB = 360.0/numsides  
    halfangleA = innerangleB/2  
  
    onehalfsideS = math.sin(math.radians(halfangleA))  
    sideS = onehalfsideS * 2  
  
    polygonCircumference = numsides * sideS  
    pi = polygonCircumference/2  
  
    return pi  
```
`Listing 2.2`  

```
>>> archimedes  
<function archimedes at 0x103e0b0>  
>>> archimedes(8)  
3.0614674589207183  
>>> archimedes(16)  
3.1214451522580524  
>>> archimedes(100)  
3.1410759078128301  
   
>>> for sides in range(8,100,8):  
        print(sides,archimedes(sides))  
```
`Listing 2.4`  
