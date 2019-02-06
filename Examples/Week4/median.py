def median(alist):
   newlist = alist[:]
   newlist.sort()
   if(len(newlist)%2 == 0):
      rightmid = len(newlist)//2
      leftmid = rightmid-1
      median = (newlist[rightmid]+newlist[leftmid])/2
   else:
      mid = len(newlist)//2
      median = newlist[mid]
   return median