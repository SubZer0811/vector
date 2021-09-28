'''
The intention of this library is to be able to perform vector operations with ease.
'''
class point2d:

	def __init__(self, pt):
		if isinstance(pt, vector2d):
			self.point = pt.vector
		if isinstance(pt, tuple):
			assert len(pt) == 2, "vector must be 2 dimensional."
			self.point = pt

	def __add__(self, b):
		if isinstance(b, point):
			return point((self.point[0]+b.point[0], self.point[1]+b.point[1], b.point[2]))
		if isinstance(b, point2d):
			return point((self.point[0]+b.point[0], self.point[1]+b.point[1]))
		if isinstance(b, vector):
			return vector((self.point[0]+b.vector[0], self.point[1]+b.vector[1], b.vector[2]))
		if isinstance(b, vector2d):
			return vector((self.point[0]+b.vector[0], self.point[1]+b.vector[1]))

	def __sub__(self, b):
		if isinstance(b, point):
			return point((self.point[0]-b.point[0], self.point[1]-b.point[1], b.point[2]))
		if isinstance(b, point2d):
			return point((self.point[0]-b.point[0], self.point[1]-b.point[1]))
		if isinstance(b, vector):
			return vector((self.point[0]-b.vector[0], self.point[1]-b.vector[1], b.vector[2]))
		if isinstance(b, vector2d):
			return vector((self.point[0]-b.vector[0], self.point[1]-b.vector[1]))

	def __str__(self):
		return f"{self.point}"

class point(object):

	def __new__(cls, pt):
		if isinstance(pt, tuple):
			if len(pt) == 2:
				return point2d(pt)
			if len(pt) == 3:
				return super(point, cls).__new__(cls)
			assert len(pt) in [2, 3], "point must be either 2 or 3 dimensional."
		if isinstance(pt, vector2d):
			return point2d(pt)
		if isinstance(pt, vector):
			return super(point, cls).__new__(cls)
		if isinstance(pt, point2d):
			return super(point, cls).__new__(cls)

	def __init__(self, pt):
		if isinstance(pt, vector):
			self.point = pt.vector
		if isinstance(pt, point2d):
			self.point = pt.point + (0,)
		if isinstance(pt, tuple):
			self.point = pt

	def __add__(self, b):
		if isinstance(b, point):
			return point((self.point[0]+b.point[0], self.point[1]+b.point[1], self.point[2]+b.point[2]))
		if isinstance(b, point2d):
			return point((self.point[0]+b.point[0], self.point[1]+b.point[1], self.point[2]))
		if isinstance(b, vector):
			return vector((self.point[0]+b.vector[0], self.point[1]+b.vector[1], self.point[2]+b.vector[2]))
		if isinstance(b, vector2d):
			return vector((self.point[0]+b.vector[0], self.point[1]+b.vector[1], self.point[2]+0))

	def __sub__(self, b):
		if isinstance(b, point):
			return point((self.point[0]-b.point[0], self.point[1]-b.point[1], self.point[2]-b.point[2]))
		if isinstance(b, point2d):
			return point((self.point[0]-b.point[0], self.point[1]-b.point[1], self.point[2]))
		if isinstance(b, vector):
			return vector((self.point[0]-b.vector[0], self.point[1]-b.vector[1], self.point[2]-b.vector[2]))
		if isinstance(b, vector2d):
			return vector((self.point[0]-b.vector[0], self.point[1]-b.vector[1], self.point[2]-0))

	def __str__(self):
		return f"{self.point}"

class vector2d:

	vector = None
	def __init__(self, v, u=None):
		
		if u == None:
			if isinstance(v, point2d):
				self.vector = v.point
			if isinstance(v, tuple):
				assert len(v) == 2, "vector must be 2 dimensional."
				self.vector = v
		else:
			if isinstance(v, point2d):
				self.vector = (v-u).point
			if isinstance(v, tuple):
				self.vector = (v[0]-u[0], v[1]-u[1])

	def __add__(self, b):
		if isinstance(b, point):
			return vector((self.vector[0]+b.point[0], self.vector[1]+b.point[1], b.point[2]))
		if isinstance(b, point2d):
			return vector((self.vector[0]+b.point[0], self.vector[1]+b.point[1]))
		if isinstance(b, vector):
			return vector((self.vector[0]+b.vector[0], self.vector[1]+b.vector[1], b.vector[2]))
		if isinstance(b, vector2d):
			return vector((self.vector[0]+b.vector[0], self.vector[1]+b.vector[1]))

	def __sub__(self, b):
		if isinstance(b, point):
			return vector((self.vector[0]-b.point[0], self.vector[1]-b.point[1], b.point[2]))
		if isinstance(b, point2d):
			return vector((self.vector[0]-b.point[0], self.vector[1]-b.point[1]))
		if isinstance(b, vector):
			return vector((self.vector[0]-b.vector[0], self.vector[1]-b.vector[1], b.vector[2]))
		if isinstance(b, vector2d):
			return vector((self.vector[0]-b.vector[0], self.vector[1]-b.vector[1]))

	def __mul__(self, b):
		if isinstance(b, vector2d):
			return (self.vector[0]*b.vector[0] + self.vector[1]*b.vector[1])
		if isinstance(b, (float, int)):
			return vector2d((self.vector[0]*b, self.vector[1]*b))

	def __rmul__(self, b):
		if isinstance(b, vector2d):
			return (self.vector[0]*b.vector[0] + self.vector[1]*b.vector[1])
		if isinstance(b, (float, int)):
			return vector2d((self.vector[0]*b, self.vector[1]*b))

	def __truediv__(self, b):
		return vector2d((self.vector[0]/b, self.vector[1]/b))
			
	def __xor__(self, b):
		return vector((0, 0, self.vector[0]*b.vector[1] - self.vector[1]*b.vector[0]))

	def __str__(self):
		return f"{self.vector[0]}i + {self.vector[1]}j"

	def magnitude(self):
		return pow(self.vector[0] ** 2 + self.vector[1] ** 2, 1/2)

class vector(object):

	vector = None
	def __new__(cls, v, u=None):
		if u == None:
			if isinstance(v, point2d):
					return vector2d(v.point)
			if isinstance(v, tuple):
				if len(v) == 2:
					return vector2d(v)
				if len(v) == 3:
					return super(vector, cls).__new__(cls)
				assert len(v) in [2, 3], "vector must be either 2 or 3 dimensional."
			if isinstance(v, (vector2d, point)):
				return super(vector, cls).__new__(cls)
		else:
			if isinstance(v, tuple):
				if max(len(u), len(v)) == 2:
					return vector2d(v, u)
				if max(len(u), len(v)) == 3:
					return super(vector, cls).__new__(cls)
			if isinstance(v, (point, point2d)):
				if max(len(u.point), len(v.point)) == 2:
					return vector2d(v, u)
				if max(len(u.point), len(v.point)) == 3:
					return super(vector, cls).__new__(cls)

	def __init__(self, v, u=None):
		if u == None:
			if isinstance(v, point):
				self.vector = v.point
			if isinstance(v, tuple):
				self.vector = v
			if isinstance(v, vector2d):
				self.vector = v.vector + (0,)
		else:
			if isinstance(v, point):
				self.vector = (v-u).point
			if isinstance(v, tuple):
				self.vector = (v[0]-u[0], v[1]-u[1], v[2]-u[2])

	def __add__(self, b):
		if isinstance(b, point):
			return point((self.vector[0]+b.point[0], self.vector[1]+b.point[1], self.vector[2]+b.point[2]))
		if isinstance(b, point2d):
			return point((self.vector[0]+b.point[0], self.vector[1]+b.point[1], self.vector[2]))
		if isinstance(b, vector):
			return point((self.vector[0]+b.vector[0], self.vector[1]+b.vector[1], self.vector[2]+b.vector[2]))
		if isinstance(b, vector2d):
			return point((self.vector[0]+b.vector[0], self.vector[1]+b.vector[1], self.vector[2]))

	def __sub__(self, b):
		if isinstance(b, point):
			return point((self.vector[0]-b.point[0], self.vector[1]-b.point[1], self.vector[2]-b.point[2]))
		if isinstance(b, point2d):
			return point((self.vector[0]-b.point[0], self.vector[1]-b.point[1], self.vector[2]))
		if isinstance(b, vector):
			return point((self.vector[0]-b.vector[0], self.vector[1]-b.vector[1], self.vector[2]-b.vector[2]))
		if isinstance(b, vector2d):
			return point((self.vector[0]-b.vector[0], self.vector[1]-b.vector[1], self.vector[2]))

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
			
	def __truediv__(self, b):
		return vector((self.vector[0]/b, self.vector[1]/b, self.vector[2]/b))

	def __xor__(self, b):
		return vector((self.vector[1]*b.vector[2] - self.vector[2]*b.vector[1], -(self.vector[0]*b.vector[2] - self.vector[2]*b.vector[0]), self.vector[0]*b.vector[1] - self.vector[1]*b.vector[0]))

	def __str__(self):
		return f"{self.vector[0]}i + {self.vector[1]}j + {self.vector[2]}k"

	def magnitude(self):
		return pow(self.vector[0] ** 2 + self.vector[1] ** 2 + self.vector[2] ** 2, 1/2)

if __name__ == "__main__":

	v1 = vector((1,1,2))
	print(v1/3)