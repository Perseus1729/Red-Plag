import re
import math
class Dimension:
    """docstring for Dimension"""
    def __init__(self,data):
        xi,yi,zi,dated=re.split(',| - ',data)
        self.x=int(xi)
        self.y=int(yi)
        self.z=int(zi)
        dd,mm,yyyy=map(int,dated.split("/"))
        self.date=(yyyy,mm,dd)
    def __str__(self):
        return "Coordinates: ({}, {}, {}) Time: ({}, {}, {})".format(self.x,self.y,self.z,self.date[0],self.date[1],self.date[2])
    def __sub__(self,other):
        if(other.date>self.date):
            return math.sqrt((self.x-other.x)**2+(self.y-other.y)**2+(self.z-other.z)**2)
        else:
            return -1
current_point=Dimension(input())
closest_point=-1
n=int(input())
minim=math.inf
for i in range(n):
    point=Dimension(input())
    dist=current_point-point
    if(dist!=-1):
        if(dist<minim):
            minim=dist
            closest_point=point
    print(point)
    #print(dist)
if(closest_point==-1):
    print("Can't move to any point")
else:
    print("Closest point is:")
    print(closest_point)