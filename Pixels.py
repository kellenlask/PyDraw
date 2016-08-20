from DrawingHelper import *
from math import *


class Pixels(BaseDrawer):
	max_pixel_depth = 5

	number_of_renders = 0

	def __init__(self, canvas):
		BaseDrawer.__init__(self, canvas)


	def draw(self):
		if self.number_of_renders > 0:
			return

		for x in range(self.width):
			for y in range(self.height):
				hue = self.get_pixel_value(x, y, 0)
				color = get_hsv(hue)
				self.set_pixel(x, y, color)

		self.number_of_renders += 1


	def get_pixel_value(self, x, y, depth):
		if depth == self.max_pixel_depth:
			return x % depth / depth

		elif (x + y) % (depth + 1) == depth / 2:
			return x * y % 360 / 360

		else:
			return self.get_pixel_value(x / 2, y * 2, depth + 1)


