# -*- coding: utf-8 -*-
from .texture import *


ICON_ALIGN_LEFT = 0
ICON_ALIGN_RIGHT = 1
ICON_ALIGN_CENTER = 2


class Icon:

	def __init__(self, path, size=[16, 16]):
		self.texture = ImageTexture(path)
		self.size = size
		self.alignment = ICON_ALIGN_LEFT