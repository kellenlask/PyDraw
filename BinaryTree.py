from DrawingHelper import *
from math import *


class BinaryTree(BaseDrawer):
	scale_ratio = 0.29
	theta = .30     # 60 degree rotations in radians
	recursion_depth = 15


	def __init__(self, canvas):
		BaseDrawer.__init__(self, canvas)


	def draw(self):
		self.draw_tree(self.recursion_depth, self.theta, self.height * 0.9, (self.width // 2, self.height - 50), -pi / 2)


	# Draws the fractal tree. order = drawings left, depth = drawings completed
	def draw_tree(self, order, angle, size, position, orientation, depth = 0):
		# Scale the size of the branch
		branch_size = size * self.scale_ratio

		# Rotate the branch
		dx = branch_size * cos(orientation)
		dy = branch_size * sin(orientation)

		# Calculate drawing coordinates
		(x, y) = position
		end_position = (x + dx, y + dy)

		# Draw the branch
		self.pen.drawLine(x, y, x + dx, y + dy)

		# If we haven't reached the bottom yet...
		if order > 0:
			# Recursively draw two new sub trees
			next_size = size * (1 - self.scale_ratio)
			self.draw_tree(order - 1, angle, next_size, end_position, orientation - self.theta * 2, depth + 1)
			self.draw_tree(order - 1, angle, next_size, end_position, orientation + self.theta / 2, depth + 1)
