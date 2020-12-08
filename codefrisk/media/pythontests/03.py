import math,re
class Dimension:
    def __init__(self,x,y,z,d):
        self.x=x
        self.y=y
        self.z=z
        self.d=d

    def __sub__(self,other):
        if(self.d[0]>other.d[0]):
            return -1
        elif(self.d[0]<other.d[0]):
            return math.sqrt((other.x-self.x)**2+(other.y-self.y)**2+(other.z-self.z)**2)
        else:
            if(self.d[1]>other.d[1]):
                return -1
            elif(self.d[1]<other.d[1]):
                return math.sqrt((other.x-self.x)**2+(other.y-self.y)**2+(other.z-self.z)**2)           
            else:
                if(self.d[2]<other.d[2]):
                    return math.sqrt((other.x-self.x)**2+(other.y-self.y)**2+(other.z-self.z)**2)
                else:
                    return -1 
    
    def __str__(self):
        return "Coordinates: {} Time: {}".format((self.x,self.y,self.z),self.d) 

x = str (input ())
list = re.split(',|- |/',x)
l = []
for i in list:
	l.append(int(i))
#https://stackoverflow.com/questions/4998629/split-string-with-multiple-delimiters-in-python
#used this link for spliting a string with multiple delimiters in former function
obj1 = Dimension(l[0],l[1],l[2],(l[5],l[4],l[3]))
n=int(input())

a = []
b = []
for i in range(n):
    y = str (input ())
    list = re.split(',|- |/',y)
    l = []
    for i in list:
            l.append(int(i))
    obj2 = Dimension(l[0],l[1],l[2],(l[5],l[4],l[3]))    
    a.append(float(obj1-obj2))
    b.append(obj2)
for i in range(n):
    print(b[i])

if(max(a)==-1):
    print("Can't move to any point")
else:
    while(a.count(-1)!=0):
        b.pop(a.index(-1))
        a.remove(-1)
    print("Closest point is:")
    print(b[a.index(min(a))])
    



