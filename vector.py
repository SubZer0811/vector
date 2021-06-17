WARNING = 0

class point2d:

	def __init__(self, point):
		assert len(point) == 2, "Point needs to be 2-dimensional"
		self.point = point

	def __add__(self, b):
		if isinstance(b, point):
			return point((self.point[0]+b.point[0], self.point[1]+b.point[1], b.point[2]))
		if isinstance(b, point2d):
			return point((self.point[0]+b.point[0], self.point[1]+b.point[1]))

	def __sub__(self, b):
		if isinstance(b, point):
			return point((self.point[0]-b.point[0], self.point[1]-b.point[1], b.point[2]))
		if isinstance(b, point2d):
			return point((self.point[0]-b.point[0], self.point[1]-b.point[1]))

	def __str__(self):
		return f"{self.point}"

class point(object):

	def __new__(cls, pt):
		if len(pt) == 2:
			if WARNING:
				print("Creating point2d object")
			return point2d(pt)
		if len(pt) == 3:
			if WARNING:
				print("Creating point3d object")
			return super(point, cls).__new__(cls)

	def __init__(self, point):
		self.point = point

	def __add__(self, b):
		if isinstance(b, point):
			return point((self.point[0]+b.point[0], self.point[1]+b.point[1], self.point[2]+b.point[2]))
		if isinstance(b, point2d):
			return point((self.point[0]+b.point[0], self.point[1]+b.point[1], self.point[2]))

	def __sub__(self, b):
		if isinstance(b, point):
			return point((self.point[0]-b.point[0], self.point[1]-b.point[1], self.point[2]-b.point[2]))
		if isinstance(b, point2d):
			return point((self.point[0]-b.point[0], self.point[1]-b.point[1], self.point[2]))

	def __str__(self):
		return f"{self.point}"

class vector2d:

	vector = None
	def __init__(self, *args):
		
		if len(args) == 1:
			assert len(args[0]) == 2, "Vector needs to be 2-dimensional"
			self.vector = args[0]

		if len(args) == 2:
			v = (args[0] - args[1])
			self.vector = (v.point[0], v.point[1])

	def __add__(self, b):
		return vector2d((self.vector[0]+b.vector[0], self.vector[1]+b.vector[1]))

	def __sub__(self, b):
		return vector2d((self.vector[0]-b.vector[0], self.vector[1]-b.vector[1]))

	def __mul__(self, b):
		if isinstance(b, vector):
			return (self.vector[0]*b.vector[0] + self.vector[1]*b.vector[1])
		if isinstance(b, (float, int)):
			return vector2d((self.vector[0]*b, self.vector[1]*b))

	def __rmul__(self, b):
		if isinstance(b, vector):
			return (self.vector[0]*b.vector[0] + self.vector[1]*b.vector[1])
		if isinstance(b, (float, int)):
			return vector2d((self.vector[0]*b, self.vector[1]*b))
			
	def __xor__(self, b):
		return vector((0, 0, self.vector[0]*b.vector[1] - self.vector[1]*b.vector[0]))

	def __str__(self):
		return f"{self.vector[0]}i + {self.vector[1]}j"

	def magnitude(self):
		return (self.vector[0] ** 2 + self.vector[1] ** 2)

class vector(object):

	vector = None
	def __new__(cls, v):
		if len(v) == 2:
			if WARNING:
				print("Creating vector2d object")
			return vector2d(v)
		if len(v) == 3:
			if WARNING:
				print("Creating vector3d object")
			return super(vector, cls).__new__(cls)

	def __init__(self, *args):
		
		if len(args) == 1:
			assert len(args[0]) == 3, "Vector needs to be 3-dimensional"
			self.vector = args[0]

		if len(args) == 2:
			v = (args[0] - args[1])
			self.vector = (v.point[0], v.point[1], v.point[2])

	def __add__(self, b):
		return vector((self.vector[0]+b.vector[0], self.vector[1]+b.vector[1], self.vector[2]+b.vector[2]))

	def __sub__(self, b):
		return vector((self.vector[0]-b.vector[0], self.vector[1]-b.vector[1], self.vector[2]-b.vector[2]))

	def __mul__(self, b):
		if isinstance(b, vector):
			return (self.vector[0]*b.vector[0] + self.vector[1]*b.vector[1] + self.vector[2]*b.vector[2])
		if isinstance(b, (float, int)):
			return vector((self.vector[0]*b, self.vector[1]*b, self.vector[2]*b))

	def __rmul__(self, b):
		if isinstance(b, vector):
			return (self.vector[0]*b.vector[0] + self.vector[1]*b.vector[1] + self.vector[2]*b.vector[2])
		if isinstance(b, (float, int)):
			return vector((self.vector[0]*b, self.vector[1]*b, self.vector[2]*b))
			
	def __xor__(self, b):
		return vector((self.vector[1]*b.vector[2] - self.vector[2]*b.vector[1], -(self.vector[0]*b.vector[2] - self.vector[2]*b.vector[0]), self.vector[0]*b.vector[1] - self.vector[1]*b.vector[0]))

	def __str__(self):
		return f"{self.vector[0]}i + {self.vector[1]}j + {self.vector[2]}k"

	def magnitude(self):
		return (self.vector[0] ** 2 + self.vector[1] ** 2 + self.vector[2] ** 2)

if __name__ == "__main__":

	p1 = vector((1, 2))
	p2 = vector((1, 1))
	# p2 = vector((3, 4))
	# p3 = vector((5, 6))
	v3 = p1^p2
	print(v3)
	print(type(v3))