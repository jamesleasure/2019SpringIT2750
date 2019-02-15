import random
import math
import os 

currentPath = os.path.dirname(os.path.realpath(__file__)) + "/"

def euclidD(point1, point2):
    sum = 0
    for index in range(len(point1)):
        diff = (point1[index]-point2[index]) ** 2
        sum = sum + diff
        
    euclidDistance = math.sqrt(sum)
    return euclidDistance

def readFile(filename):
    currentPath = os.path.dirname(os.path.realpath(__file__)) + "/"
    filepath = currentPath + filename
    datafile = open(filename, "r")
    datadict = {}

    key = 0
    for aline in datafile:
       key = key + 1
       score = int(aline)

       datadict[key] = [score]   
       
    return datadict

# STEP 2 of the K-Means Cluster Analysis Algorithm:
#   Randomly choose k of the data points to serve as the initial centroids for the k clusters.
#   Parameters:
#      k - the number of clusters we'll create. This is chosen number from STEP 1.
#      datadict is a list with all of the values from our file input. In this case it's grade percentages.
def createCentroids(k, datadict):
    centroids=[]           
    centroidCount = 0
    centroidKeys = []

    # We will loop until < k - remember k is the number of random centroids we will create from step 1
    while centroidCount < k:
       # We use the random class to generate a random index from our data dictionary of values
       rkey = random.randint(1,len(datadict))
       if rkey not in centroidKeys:
           # We store the centroid in a dictionary called centroidKeys to make sure we don't reuse it
           centroids.append(datadict[rkey])   
           centroidKeys.append(rkey)       
           centroidCount = centroidCount + 1   
           
    return centroids
    
# STEP 3 of the K-Means Cluster Analysis Algorithm
def createClusters(k, centroids, datadict, repeats):
    for apass in range(repeats):
        print("****PASS",apass,"****")
        clusters = []                      
        for i in range(k):
           clusters.append([])             

        # the outer loop loops through every value from the file input (all grades)
        for akey in datadict:
           distances = []              
           # a nested loop, loops through each cluster value. We then calculate the distance of each cluster value to each point.       
           for clusterIndex in range(k): 
               # We use euclidD to calculate a distance for each cluster in comparison to each data point.   
               dist = euclidD(datadict[akey],centroids[clusterIndex])
               distances.append(dist)       

           # we append the minimum distance to the variable mindist. mindist contains the value of the distance.
           mindist = min(distances)         
           # index is grabbing the index of the value in the data dictionary.
           # index refers to the cluster that we're assigning the value from datadict to.
           index = distances.index(mindist)  

           # akey is just incrementing 0<k. We're appending the index of the data item to clusters for cluster.
           # So, we might have something like:
           #  CLUSTER 0 or clusters[0] or clusters key 0
           #  KEY for value at CLUSTER 0 = [34, 56, 44, 45, 34, 45]
           #      note that each key in the dictionary contains a list of values. These are the points that are part of the cluster.
           clusters[index].append(akey)     

        # STEP 2b: Recompute the centroids for each cluster
        dimensions = len(datadict[1])  
        # Loop through each cluster    
        for clusterIndex in range(k):      
           sums = [0]*dimensions
           # Loop through each value in the current cluster
           # calculate a new centroid based on the current values in the cluster
           for akey in clusters[clusterIndex]:
               datapoints = datadict[akey]
               for ind in range(len(datapoints)):           
                   sums[ind] = sums[ind] + datapoints[ind]  
           for ind in range(len(sums)):                    
               clusterLen = len(clusters[clusterIndex])
               if clusterLen != 0:
                  sums[ind] = sums[ind]/clusterLen   
       
           centroids[clusterIndex] = sums   
           
        for c in clusters:          
           print ("CLUSTER")
           for key in c:
               print(datadict[key], end=" ")
           print()                     
           
    return clusters


newcurrentPath = os.path.dirname(os.path.realpath(__file__)) + "/"
examsFile = newcurrentPath + "cs150exams.txt"
dd=readFile(examsFile)
# STEP 1 of K-Means Cluster Analysis: Choose k for number of clusters. k=5.
# STEP 2 - See the algortithm fro createCentroids() to see the details for step 2.
c=createCentroids(5,dd)

cl=createClusters(5,c,dd,9)
print(cl)