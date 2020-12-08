import math


class Dimension:

	def __init__(self):

		x=input()
		str1=x.split(' - ')
		str2=str1[0].split(',')
		str3=str1[1].split('/')

		self.x=int(str2[0])	
		self.y=int(str2[1])	
		self.z=int(str2[2])	
		self.d=(int(str3[2]),int(str3[1]),int(str3[0]))

	def __sub__(self,a):

		if self.d[0]>a.d[0] or (self.d[0]==a.d[0] and self.d[1]>a.d[1]) or (self.d[0]==a.d[0] and self.d[1]==a.d[1] and self.d[2]>a.d[2]):	
			return math.sqrt((self.x-a.x)**2+(self.y-a.y)**2+(self.z-a.z)**2)
		else:
			return -1

	def __str__(self):

		x='Coordinates: ('+str(self.x)+', '+str(self.y)+', '+str(self.z)+') Time: ('+str(self.d[0])+', '+str(self.d[1])+', '+str(self.d[2])+')'
		return x


obj=Dimension()

n=int(input())

list_obj=[]

min_index=-1
min_value=-1
for i in range(n):
	list_obj.append(Dimension())
	diff=list_obj[i]-obj
	if (diff<min_value or min_value==-1) and diff!=-1:
		min_value=diff
		min_index=i



for i in range(n):
	print(str(list_obj[i]))

if min_value!=-1:
	print('Closest Point is:')
	print(str(list_obj[min_index]))
else:
	print("Can't move to any point")

