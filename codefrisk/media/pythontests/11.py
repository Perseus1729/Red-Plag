class Dimension:
	def __init__(self,s):
		templist=s.split(",")
		s2=(templist[2])
		list2=s2.split(" - ")
		s3=list2[1]
		self.x=int(templist[0])
		self.y=int(templist[1])
		self.z=int(list2[0])
		self.d=[int(abc) for abc in s3.split("/")]
		self.d.reverse()
		#self.d=list3.reverse()
	def show(self):
		print(self.x,self.y,self.z,self.d)
	def __lt__(self,other):
		if self.d[0]!= other.d[0]:
			if self.d[0]< other.d[0]:
				return True
			else:
				return False
		elif self.d[1]!= other.d[1]:
			if self.d[1]< other.d[1]:
				return True
			else:
				return False
		else:
			if self.d[2]< other.d[2]:
				return True
			else:
				return False
	def __sub__(self,other):
		if self<other:
			d=((other.x-self.x)**2+(other.y-self.y)**2+(other.z-self.z)**2)**(0.5)
			return d
		else:
			return -1
	def __str__(self):
		return 'Coordinates: ('+str(self.x)+', '+str(self.y)+', '+str(self.z)+') Time: ('+str(self.d[0])+', '+str(self.d[1])+', '+str(self.d[2])+')'

x=str(input())
cur=Dimension(x)
n=int(input())
a=[]
for j in range(n):
	x=str(input())
	y=Dimension(x)
	a.append(y)
minimum=-1
closestpoint=0
for j in range(n):
	print(a[j])
	dist=cur - a[j]
	if dist!=-1:
		if minimum!=-1:
			if dist<minimum:
				minimum=dist
				closestpoint=a[j]
		else:
			minimum=dist
			closestpoint=a[j]
if minimum!=-1:
	print("Closest point is:")
	print(closestpoint)
else:
	print("Can't move to any point")	

# tp1=Dimension("1,2,3 - 10/10/2000")
# tp2=Dimension("1,2,3 - 1/10/2000")
# print(tp1)
# x=tp1-tp2
# tp1.show()
# print("X",x)


