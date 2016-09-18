# -*- coding: utf-8 -*-
from .texture import *
from .font import *
from .rect import *


class Style:

	def __init__(self, skinPath=None, fontPath=None):
		self.skin = ImageTexture(skinPath)
		self.font = Font(fontPath)

		self.offset = 4

	#    0    1    2    3    4
	# +----+----+----+----+----+
	# |NORM|CLIC|HOVE|INAC|CUST|
	# | AL | K  | R  |TIVE| OM | 0 PANEL
	# +----+----+----+----+----+
	# |    |    |    |    |    |
	# |    |    |    |    |    | 1 BUTTON
	# +----+----+----+----+----+
	# |    |    |    |    |    |
	# |    |    |    |    |    | 2 CHECK
	# +----+----+----+----+----+
	# |    |    |    |    |    |
	# |    |    |    |    |    | 3 RADIO
	# +----+----+----+----+----+
	# |    |    |    |    |    |
	# |    |    |    |    |    | 4 ENTRY
	# +----+----+----+----+----+
	# |    |    |    |    |    |
	# |    |    |    |    |    | 5 SLIDER
	# +----+----+----+----+----+
	def getTextureRegion(self, ctype, cstate):
		row = ctype
		col = cstate

		w = 1.0 / 5
		h = 1.0 / 6

		return Rect(col * w, row * h, w, h)