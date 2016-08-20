#!/usr/bin/python

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import BinaryTree
import Mandelbrot
import Circles
import Pixels

# I like programs that leverage math to draw things on the screen; however, such projects are usually too small to
# package on their own. To get the best of both worlds (writing fun drawing programs, and making reasonable packages)
# this project will package all such programs together with a little selection box or something to select the drawing
# run.
#
# Basic Approach:
#   Write a single file to handle the UI drawing side, and which can load in the draw-ers stored in other files.as


window_height = 1000
window_width = 1600
window_background_color = (53, 70, 92)

combo_box_options = [
	'Circles',
	'Binary Tree',
	'Pixels',
	'Mandelbrot',

]

combo_box_actions = [
	Circles.Circles,
	BinaryTree.BinaryTree,
	Pixels.Pixels,
	Mandelbrot.Mandelbrot,
]


class Interface(QWidget):

	def __init__(self, parent=None):
		# Window setup
		super(Interface, self).__init__(parent)
		self.showMaximized()

		# Setup combobox
		self.combobox = QComboBox()
		self.combobox.addItems(combo_box_options)
		self.combobox.currentIndexChanged.connect(self.onSelectionChanged)
		self.combobox.setParent(self)
		self.combobox.show()


	def paintEvent(self, event):
		index = self.combobox.currentIndex()
		combo_box_actions[index](self).draw()


	def onSelectionChanged(self, index):
		self.repaint()


if __name__ == '__main__':
	import sys

	app = QApplication(sys.argv)

	screen = Interface()
	screen.show()

	sys.exit(app.exec_())