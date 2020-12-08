class Dimension:
	def __init__(self,str):
		string_list=str.split(' - ')
		coordi=string_list[0].split(',')
		self.x=int(coordi[0])
		self.y=int(coordi[1])
		self.z=int(coordi[2])
		self.d=[]
		
		date=string_list[1]
		li=date.split('/')
		self.d.append(int(li[2]))
		self.d.append(int(li[1]))
		self.d.append(int(li[0]))
	def __sub__(self,other):
		od=other.d
		sd=self.d
		if od[0] < sd [0]:
			return -1
		elif od[0] == sd[0]:
			if od[1] < sd[1]:
				return -1
			elif od[1]==sd[1]:
				if od[2] > sd[2]:
					return ((((self.x - other.x)**2)+((self.y - other.y)**2)+((self.z - other.z)**2))**.5)
				else:
					return -1
			else:
				return ((((self.x - other.x)**2)+((self.y - other.y)**2)+((self.z - other.z)**2))**.5)
		else:
			return ((((self.x - other.x)**2)+((self.y - other.y)**2)+((self.z - other.z)**2))**.5)
		
	def __str__(self):
		dl=self.d
		return 'Coordinates: ({0}, {1}, {2}) Time: ({3}, {4}, {5})'.format(self.x,self.y,self.z,dl[0],dl[1],dl[2])
		# print(d)
		# print(coordi)
		# print(li)
	# def __str__(self):

s=input()
ob=Dimension(s)
n = int(input())
k = []
ld = []
min=-1
for i in range(n):
	m=input()
	k.append(m)
for i in k:
	o=Dimension(i)
	print(o)
	if (ob - o) == -1:
		continue
	else:
		if min==-1:
			min=ob-o
			obmin=o
		elif (ob - o) < min:
			min=ob - o
			obmin=o
if min ==-1:
	print('Can\'t move to any point')
else:
	print('Closest point is:')
	print(obmin)




