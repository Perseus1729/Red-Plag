import math
class Dimension():
	"""docstring for ClassName"""
	def __init__(self, x,y,z,d):
		self.d=tuple(d)
		self.c=(x,y,z)
		self.int_d=[int(x) for x in self.d]
		self.int_c=[int(x) for x in self.c]
	def __str__(self):
		coor="("+', '.join(self.c)+")"
		date="("+', '.join([str(x) for x in self.int_d])+")"
		return "Coordinates: "+coor+" Time: "+date
	def dateCheck(self,other):
		for i in range(0,len(self.int_d)):
			if(other.int_d[i]>self.int_d[i]):
				return True
			elif(other.int_d[i]<self.int_d[i]):
				return False
		return False
	def __sub__(self,other):
		if(self.dateCheck(other)):
			distsq=sum([(i-j)*(i-j) for i,j in zip(self.int_c,other.int_c)])
			return distsq
		else:
			return -1

a=input().rsplit(' - ',1)
coordinates=a[0].split(',')
date=a[1].split('/')
date.reverse()
curr_pos=Dimension(*coordinates,date)

n=int(input())
minpos=curr_pos
min_dis=-1

listinputs=[]
for i in range(0,n):
	a=input()
	listinputs.append(a)
for b in listinputs:
	a=b.rsplit(' - ',1)
	coordinates=a[0].split(',')
	date=a[1].split('/')
	date.reverse()
	new_pos=Dimension(*coordinates,date)
	print(new_pos)
	curr_dis= curr_pos - new_pos
	if(min_dis==-1):
		min_dis=curr_dis
		minpos=new_pos
	elif(curr_dis<min_dis and curr_dis>=0):
		min_dis=curr_dis
		minpos=new_pos

if(min_dis==-1):
	print("Can't move to any point")
else:
	print("Closest point is:")
	print(minpos)