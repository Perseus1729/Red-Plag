import math
import sys
class Dimension :
	def __init__(self,s):
		s1=s.split(",")
		s2=s1[2].split("-")
		t=tuple(s2[1].split("/"))
		self.x=int(s1[0])
		self.y=int(s1[1])
		self.z=int(s2[0])
		self.d=(int(t[2]),int(t[1]),int(t[0]))

	def __sub__(self,o):
		x1=self.x-o.x
		y1=self.y-o.y
		z1=self.z-o.z
		if(self.d<o.d):
			return math.sqrt(x1*x1+y1*y1+z1*z1)
		else:
			return -1

	def __str__(self):
		t=(self.x,self.y,self.z)
		ans="Coordinates: "+str(t)+" Time: "+str(self.d)
		return ans

s=input()
x=input()
i=0
y=sys.maxsize
o=Dimension(s)
output=""
output2=""
while(i<int(x)):
	a=input()
	on=Dimension(a)
	output+=on.__str__()+"\n"
	z=o-on
	if(z!=-1):
		y=min(y,z)
		if(y==z):
			output2=on.__str__()
	i+=1
print(output.strip())
if(y==sys.maxsize):
	print("Can't move to any point")
else:
	print("Closest point is:")
	print(output2)
		