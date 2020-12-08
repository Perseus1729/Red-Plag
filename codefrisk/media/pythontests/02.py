class Dimension:
	def __init__(self,string):
		a,b=string.split(' - ')
		c=a.replace(' ','')
		e=c.split(',')
		l=b.replace(' ','').split('/')
		l1=[int(i) for i in l]
		l2=l1[::-1]
		l3=tuple(l2)
		self.x=int(e[0])
		self.y=int(e[1])
		self.z=int(e[2])
		self.d=l3

	def __sub__(self,obj2):
		if(self.d[0]>obj2.d[0]):
			return -1
		elif(self.d[0]==obj2.d[0]):
			if(self.d[1]>self.d[1]):
				return -1
			elif(self.d[1]==obj2.d[1]):
				if(self.d[2]>=obj2.d[2]):
					return -1
				else:
					import math
					return math.sqrt(((self.x-obj2.x)**2)+((self.y-obj2.y)**2)+((self.z-obj2.z)**2))
			else:
				import math
				return math.sqrt(((self.x-obj2.x)**2)+((self.y-obj2.y)**2)+((self.z-obj2.z)**2))
		else:
			import math
			return math.sqrt(((self.x-obj2.x)**2)+((self.y-obj2.y)**2)+((self.z-obj2.z)**2))

	def __str__(self):
		print('Coordinates:',tuple([self.x,self.y,self.z]),'Time:',self.d)

x=input()
n=int(input())
x1=Dimension(x)
strings=[]
for i in range(n):
	str1=input()
	strings.append(str1)
#print(strings)
dims=[]
for i in range(n):
	ds=Dimension(strings[i])
	dims.append(ds)

[c.__str__() for c in dims]
y=[(x1-i) for i in dims]
def no(l):
	count=0
	for x in l:
		if x == -1:
			count+=1
	return count

def posOfmin(l):
	mini=1000000
	for x in l:
		if x < mini and x != -1:
			mini=x
	for i in range(n):
		if l[i] == mini:
			return i


if no(y) == n:
	print("Can't move to any point")
else:
	print("Closest point is:")
	dims[posOfmin(y)].__str__()


























