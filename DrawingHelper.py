from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from enum import Enum


# An Enum to abstract out the QBrush shenanigans
class Color(Enum):
	white = QBrush(Qt.white)
	black = QBrush(Qt.black)
	red = QBrush(Qt.red)
	darkRed = QBrush(Qt.darkRed)
	green = QBrush(Qt.green)
	darkGreen = QBrush(Qt.darkGreen)
	blue = QBrush(Qt.blue)
	darkBlue = QBrush(Qt.darkBlue)
	cyan = QBrush(Qt.cyan)
	darkCyan = QBrush(Qt.darkCyan)
	magenta = QBrush(Qt.magenta)
	darkMagenta = QBrush(Qt.darkMagenta)
	yellow = QBrush(Qt.yellow)
	darkYellow = QBrush(Qt.darkYellow)
	grey = QBrush(Qt.gray)
	darkGrey = QBrush(Qt.darkGray)
	lightGrey = QBrush(Qt.lightGray)
	transparent = QBrush(Qt.transparent)



class BaseDrawer:
	@property
	def width(self):
		return self.canvas.width()


	@property
	def height(self):
		return self.canvas.height()


	@property
	def center(self):
		return (self.width / 2, self.height / 2)


	def __init__(self, canvas):
		self.canvas = canvas

		self.pen = QPainter(canvas)
		self.pen.setRenderHint(QPainter.Antialiasing)

		self.set_pen(get_color("#7F8A98"))
		self.set_background(get_color("#35465C"))


	def set_fill(self, color):
		self.pen.setBrush(QBrush(color))


	def set_pen(self, color):
		self.pen.setPen(color)


	def set_background(self, color):
		self.pen.fillRect(0, 0, self.canvas.width(), self.canvas.height(), color)


	def set_pixel(self, x, y, color):
		old_color = self.pen.pen().color()
		self.set_pen(color)

		self.pen.drawPoint(x, y)

		self.set_pen(old_color)


	def draw_circle(self, x, y, radius):
		point = QPoint(x, y)
		self.pen.drawEllipse(point, radius, radius)





def get_hsv(h, s = 1, v = 1):
	return_color = QColor()
	return_color.setHsvF(h, s, v)

	return return_color


def get_color(color):
	return_color = QColor()
	return_color.setNamedColor(color)

	return return_color


