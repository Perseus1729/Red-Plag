import math
def compare(d1,d2):
	for i in reversed(range(3)):
		if(d1[i]>d2[i]):
			return True
	return False



class Dimension:
	def __init__(self,s):
		[a,b,c]=s.split(" ")
		[self.x,self.y,self.z]=[int(v) for v in a.split(",")]
		self.d=[int(x) for x in c.split("/")]

	def dist(self,other):
		return math.sqrt(((self.x-other.x)**2+(self.y-other.y)**2+(self.z-other.z)**2))

	def __sub__(self,other):
		if compare(other.d,self.d):
			return self.dist(other)
		else:
			return -1
	def __str__(self):
		return "Coordinates: ("+str(self.x)+","+str(self.y)+","+str(self.z)+") Time: ("+str(self.d[2])+","+str(self.d[1])+","+str(self.d[0])+")"

a=str(input())
c_d=Dimension(a)
n=int(input())
list_c_d=[]
min_distance=-1
mini=c_d

for i in range(n):
	b=str(input())
	c=Dimension(b)
	list_c_d.append(c)
	distance=c_d-c
	if distance!=-1:
		if distance<min_distance or min_distance==-1:
			min_distance=distance
			mini=c
for i in list_c_d:
	print(i)

if min_distance==-1:
	print("Can't move to any point")
	#print(min_distance)
else:
	print("Closest point is:")
	print(mini)