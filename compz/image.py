# -*- coding: utf-8 -*-
from .component import *
from .texture import *
from .gfx import *


IMG_SCALE_FIT = 0
IMG_SCALE_STRETCH = 1
IMG_SCALE_NONE = 2


class Image(Component):

	def __init__(self, path="", style=None):
		super(Image, self).__init__(style)
		self.texture = ImageTexture(path,
							interp_mode=GL_LINEAR) if len(path) > 0 else None
		self.scaleMode = IMG_SCALE_FIT

	def draw(self):
		Component.draw(self)

		if self.texture is not None:
			_b = self.transformedBounds()
			_b.x += 4
			_b.y += 4
			_b.width -= 8
			_b.height -= 8

			b = self.transformedBounds()

			self.system.gfx.clipBegin(_b.x, _b.y, _b.width, _b.height)
			iw, ih = self.texture.size
			w, h = b.width, b.height

			fw, fh = iw, ih
			if self.scaleMode == IMG_SCALE_FIT:
				aspect = min(w / iw, h / ih)
				fw = iw * aspect
				fh = ih * aspect
			elif self.scaleMode == IMG_SCALE_STRETCH:
				fw, fh = w, h
			x = b.x + w / 2 - fw / 2
			y = b.y + h / 2 - fh / 2

			self.system.gfx.drawQuad(x, y, fw, fh, texture=self.texture)
			self.system.gfx.clipEnd()