class Dimension:
	def __init__(self,string):
		a=string.split(sep=',')
		self.x=int(a[0])
		self.y=int(a[1])
		b=a[2].split(sep=' - ')
		self.z=int(b[0])
		c=b[1].split(sep='/')
		self.d=[int(c[2]),int(c[1]),int(c[0])]
	def __sub__(self, other):
		dummy=0
		if self.d[0]<other.d[0]:
			dummy=1
		elif self.d[0]>other.d[0]:
			dummy=0
		else:
			if self.d[1]<other.d[1]:
				dummy=1
			elif self.d[0]>other.d[0]:
				dummy=0
			else:
				if self.d[2]<other.d[2]:
					dummy=1	
		if dummy==1:	
			return pow((self.d[0]-other.d[0]),2)+pow((self.d[1]-other.d[1]),2)+pow((self.d[2]-other.d[2]),2)
		else:
			return -1
	def __str__(self):
		return 'Coordinates: '+ '(' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ')' + ' Time: ' + '(' + str(self.d[0]) + ', ' + str(self.d[1]) + ', ' + str(self.d[2]) + ')'
string=input()
currentpoint=Dimension(string)
#print(currentpoint)
n=int(input())
minimum=10000000
store=currentpoint
for i in range(n):
	str1=input()
	nextpoint=Dimension(str1)
	print(nextpoint)
	a=currentpoint - nextpoint
	if a!=-1 and a<minimum:
			minimum=a
			store=nextpoint
if minimum==10000000:
	print("Can't move to any point")
else:
	print("Closest point is:")
	print(store)



			
				




            