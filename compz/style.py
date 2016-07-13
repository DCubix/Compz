# -*- coding: utf-8 -*-
from .texture import *
from .font import *


class Style:

	def __init__(self, name="Component", stylesPath=None, fontPath=None):
		sp = stylesPath
		n = name
		self.textures = {
			"normal": ImageTexture(sp + n + "_normal.png") if sp is not None else None,
			"clicked": ImageTexture(sp + n + "_clicked.png") if sp is not None else None,
			"hover": ImageTexture(sp + n + "_hover.png") if sp is not None else None,
			"inactive": ImageTexture(sp + n + "_inactive.png") if sp is not None else None
		}
		self.font = Font(fontPath)

		self.offset = 4
		self.size = 16