from DrawingHelper import *
from math import *


class Circles(BaseDrawer):
	depth = 10

	def __init__(self, canvas):
		BaseDrawer.__init__(self, canvas)


	def draw(self):
		x = self.width / 2
		y = self.height / 2

		self.draw_circles(x, y, y, 0)


	def draw_circles(self, x, y, radius, depth):
		self.draw_circle(x, y, radius)

		if depth < self.depth:
			self.draw_circles(x + radius, y, radius / 2, depth + 1)
			self.draw_circles(x - radius, y, radius / 2, depth + 1)
