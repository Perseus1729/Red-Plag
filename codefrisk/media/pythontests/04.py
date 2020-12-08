import math

class Dimension:
	def __init__(self, s):
		s = s.split(" - ")
		coords = list(map(int, s[0].split(',')))
		date = tuple(map(int, reversed(s[1].split('/'))))
		self.d = date
		self.x = coords[0]
		self.y = coords[1]
		self.z = coords[2]
	def __sub__(self, other):
		if self.d < other.d:
			diff_x = self.x - other.x
			diff_y = self.y - other.y
			diff_z = self.z - other.z
			return math.sqrt(diff_x ** 2 + diff_z ** 2 + diff_y ** 2)
		else:
			return -1
	def __str__(self):
		return "Coordinates: (" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ") Time: " + str(self.d)

init = Dimension(input())
n = int(input())
min_distance = -1
closest = -1
lt = []
for i in range(n):
	s = Dimension(input())
	lt.append(s)

	if min_distance == -1 and init - s != -1:
		min_distance = init - s
		closest = s
	else:
		if init - s != -1:
			if init - s < min_distance:
				min_distance = init - s
				closest = s
for i in lt:
	print(i)

if min_distance == -1:
	print("Can't move to any point")
else:
	print("Closest point is: ")
	print(closest)
