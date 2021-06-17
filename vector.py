class point:

	def __init__(self, point):
		assert len(point) == 3, "Point needs to be 3-dimensional"
		self.point = point

	def __add__(self, b):
		return point((self.point[0]+b.point[0], self.point[1]+b.point[1], self.point[2]+b.point[2]))

	def __sub__(self, b):
		return point((self.point[0]-b.point[0], self.point[1]-b.point[1], self.point[2]-b.point[2]))

	def __str__(self):
		return f"{self.point}"

class vector:

	vector = None
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
			return (self.vector[0]*b, self.vector[1]*b, self.vector[2]*b)
			
	def __xor__(self, b):
		return (self.vector[1]*b.vector[2] - self.vector[2]*b.vector[1], -(self.vector[0]*b.vector[2] - self.vector[2]*b.vector[0]), self.vector[0]*b.vector[1] - self.vector[1]*b.vector[0])

	def __str__(self):
		return f"{self.vector}"

	def magnitude(self):
		return (self.vector[0] ** 2 + self.vector[1] ** 2 + self.vector[2] ** 2)

if __name__ == "__main__":

	p1 = point((1,2,3))
	p2 = point((4,2,3))
	
	u = vector(p1, p2)
	v = vector((2, 4, 2))