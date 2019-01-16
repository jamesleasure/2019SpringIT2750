## IT 2750 - Lab 2

*Use Chapter 2 to complete this lab.*

1. Create a folder in your repository called Lab2.
2. In the Lab 2 folder add a file called README.md. Note: create all of the following files in the lab 2 folder.
3. In your README.md file, describe - in a few sentences - what we've covered in lesson 2. 
4. Again, in README.md, answer the following questions:
5. Create a file called archimedes.py. In archimedes.py, implement the archimedes in Listings 2.2 and 2.4 in the chapter. 2.7 Modify the archimedes function to take the radius as a parameter. Can you get a better answer more quickly using a larger circle?
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
 
6. Create a file called Stats100.py. Create functions to complete the following:
    2.8 Compute the sum of the first 100 even numbers. Call the function First100EvenSum.
    2.9 Compute the sum of the first 50 odd numbers. Call the function First50OddSum.
    2.10 Compute the average of the first 100 odd numbers. Call the function First100Avg.
7. Create a file called boolean.py. (2.27) Write a compound Boolean expression that returns True if the value of the variable count is between 1 and 10 inclusive. Run the expression with a value of 1, 5, 9, 10, and 12. Output the value of count and the return value for each.
8. Create a file called ifelse.py. (2.30) Write a nested selection using ifelse that sets the value of a variable gradepoint to 4 if a variable named score is greater than 90, 3 if score is between 80 and 89, 2 if score is between 70 and 79, 1 if score is between 60 and 69, and 0 otherwise.
