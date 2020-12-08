class Dimension:
    def __init__(self, s):
        s = s.split(" - ")
        c = s[0].split(",")
        t = s[1].split("/")
        self.Time = []
        self.Time.append(int(t[2]))
        self.Time.append(int(t[1]))
        self.Time.append(int(t[0]))
        self.x = int(c[0])
        self.y = int(c[1])
        self.z = int(c[2])
    def __str__(self):
        out = "Coordinates: ("+str(self.x)+", "+str(self.y)+", "+str(self.z)+") Time: ("+str(self.Time[0])+", "+str(self.Time[1])+", "+str(self.Time[2])+")"
        return out
    def __sub__(self, other):
        if (self.Time[0] > other.Time[0]):
            return -1
        if (self.Time[0] == other.Time[0]) and (self.Time[1] > other.Time[1]):
            return -1
        if (self.Time[0] == other.Time[0]) and (self.Time[1] == other.Time[1]) and (self.Time[2] >= other.Time[2]):
            return -1
        delX2 = (self.x-other.x)**2
        delY2 = (self.y-other.y)**2
        delZ2 = (self.z-other.z)**2
        return (delX2+delY2+delZ2)**(1/2)
s = input()
D = Dimension(s)
n = int(input())
Candidates = []
for i in range(n):
    t = input()
    E = Dimension(t)
    Candidates.append(E)
m = 0
valid_dims = []
for i in Candidates:
    print(i)
    if (D-i != -1):
        m = m+1
        valid_dims.append(i)
if (m==0):
    print("Can't move to any point")
    exit()
champion = valid_dims[0]
minimum = D-valid_dims[0]
for i in valid_dims:
    challenger = i
    if (D-i < minimum):
        champion = challenger
        minimum = D-i
print("Closest point is:")
print(champion)
