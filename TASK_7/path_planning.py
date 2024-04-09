import cv2
import matplotlib.image as plt
import matplotlib.pyplot as pllt
import numpy as np
import heapq
from collections import deque
import math
import time
PI=22/7

def astar(grid,start,goal):

    
    def h(cell1,cell2):
        return abs(cell1[0]-cell2[0])+abs(cell1[1]-cell2[1])

    def adjacentcell(grid,currentcell,current_gscore,goal):
        rows,cols=5,5

        minfscore=100000
        
        for i in range(4):
            
            #print(currentcell)
           # print(currentcell[1])
            #time.sleep(2)
            
            rowcheck=currentcell[0]+int(round(math.sin((PI/2)*i)))
            colcheck=currentcell[1]+int(round(math.cos((PI/2)*i)))
            #print(int(round(math.sin((PI/2)*i))),int(round(math.cos((PI/2)*i))))
            #print(rowcheck,colcheck)
            
            if not(0<=rowcheck<rows and 0<=colcheck<cols):
                
                continue

            elif (rowcheck,colcheck)==goal:
                return goal

            elif grid[rowcheck][colcheck]==0:
                
                continue
            
            #time.sleep(2)
            
            f_score=h((rowcheck,colcheck),goal)+(current_gscore+1)

            if f_score<minfscore:
                minfscore=f_score

        for i in range(4):
            rowcheck=currentcell[0]+int(round(math.sin((PI/2)*i)))
            colcheck=currentcell[1]+int(round(math.cos((PI/2)*i)))
            
            if not(0<=rowcheck<rows and 0<=colcheck<cols):
                continue
            elif (rowcheck,colcheck)==goal:
                return goal
            elif grid[rowcheck][colcheck]==0:
                continue
            
            f_score=h((rowcheck,colcheck),goal)+(current_gscore+1)

            if f_score==minfscore:
                #print(rowcheck,colcheck)
                return (rowcheck,colcheck)
            
    goalreached=False
    currentcell=(0,0)
    #print(currentcell)
    
    path=[(0,0),]
    current_gscore=0
    while not goalreached:

    
        currentcell=adjacentcell(grid,currentcell,current_gscore,goal)
        path.append(currentcell)
        if currentcell==goal:
            goalreached=True
            return path
        current_gscore+=1

imagepath=r"C:\Users\chint\AppData\Local\Programs\Python\Python310\Summer Project Robotics Club Task\Screenshot 2024-04-08 095210.png"
image=cv2.imread(imagepath)
img=plt.imread(imagepath)

image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
se=cv2.getStructuringElement(cv2.MORPH_RECT,(8,8))

bg=cv2.morphologyEx(image,cv2.MORPH_DILATE,se)
out_gray=cv2.divide(image,bg,scale=255)

out_binary=cv2.threshold(out_gray,0,255,cv2.THRESH_OTSU)[1]

bwimg=np.array(out_binary)
c=[]

for i in range(5):
    d=[]
    for j in range(5):
        #print(sum(sum(bwimg[172*i:172*(i+1),172*j:172*(j+1)])))
        if(sum(sum(bwimg[172*i:172*(i+1),172*j:172*(j+1)])))>17000:
            d.append(0)

        else:
            d.append(1)

    c.append(d)
        
grid=c
#print(grid)
#print(grid[1][2])

start=(0,0)
goal=(4,4)
path=astar(grid,start,goal)

print("Shortest Path : ")
print(path)
       
        
    
