First , Write Code to Scan grid image and convert it to 2-D array in python , assigning 1 at all index where grid colour is yellow and at those index where
box is blue assign 0 at those indexes .

And for finding the shortest path from starting point (1,1) to goal (5,5) . I am using A* Algorithm , what i am actually doing is that ,
From starting point , we are looking to adjacent cells in all 4 dirn ,if  that  is not blocked cell coordinate of adjacent cell is not out of range , then
I am calculating Heuristic in that allowed adjacent cell and out of those allowed adjacent cells i am moving to one  in which heuristic is least , and 
return it to variable "current_cell" and simultaneously I will store this coordinates in a list named "shortest_path" . In these way I will 
repeat the process untill I reached a cell which is goal . Once I treached the goal , I will put the coordinate of goal in "shortest_path" list and 
return it . 

And after the coordinates of shortest path , we will print the image of coordinates over grid image . we will create the block surface over which 
we will write the coordinates . and  will place the that block surface over origional grid image .
