from DrawingHelper import *
from math import *


class Mandelbrot(BaseDrawer):

	# Mandelbrot settings
	min_value = -.5
	max_value = .5


	def __init__(self, canvas):
		BaseDrawer.__init__(self, canvas)


	def draw(self):
		# For each pixel in the canvas
		for x in range(self.width):
			for y in range(self.height):
				# Normalize X, Y into our window
				x_norm = ((x / self.width) * (self.max_value - self.min_value)) - self.min_value
				y_norm = ((y / self.height) * (self.max_value - self.min_value)) - self.min_value

				x1 = 0
				y1 = 0

				iteration = 0

				while x1 ** 2 + y1 ** 2 < 4 and iteration < 1000:
					xtemp = x1 ** 2 - y ** 2 + x_norm
					y1 = 2 * x1 * y + y_norm
					x1 = xtemp
					iteration += 1

				hue = iteration % 1.0

				print(hue)
				#self.set_pen(get_hsv(hue))
				#self.pen.drawPoint(x, y)


	@staticmethod
	# Returns a color based on the Mandelbrot function's behavior at that point
	def value_for_pixel(c):
		for i in range(360):
			if True:
				pass


			z = z * z + c

			if abs(z) > 2:
				return i

		return 360
