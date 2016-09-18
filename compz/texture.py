# -*- coding: utf-8 -*-
"""
@author: Moguri
@modified: TwisterGE
"""
from bge import texture

from .gfx import *


class Texture:
	def __init__(self, path, interp_mode):
		self._tex_id = glGenTexture()
		self.size = [0, 0]
		self._interp_mode = None
		self.path = None
		self.valid = True

		self.bind()
		glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)
		self.interp_mode = interp_mode

		self.reload(path)

	def __del__(self):
		glDeleteTextures([self._tex_id])

	@property
	def interp_mode(self):
		return self._interp_mode

	@interp_mode.setter
	def interp_mode(self, value):
		if value != self._interp_mode:
			self.bind()
			glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, value)
			glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, value)
			self._interp_mode = value

	def bind(self, loc=0):
		glActiveTexture(GL_TEXTURE0 + loc)
		glBindTexture(GL_TEXTURE_2D, self._tex_id)

	@staticmethod
	def unbind():
		glBindTexture(GL_TEXTURE_2D, 0)


class ImageTexture(Texture):

	_cache = {}

	def __init__(self, image, interp_mode=GL_NEAREST, caching=True):
		self._caching = caching
		super().__init__(image, interp_mode)

	def reload(self, image):
		if image == self.path:
			return

		if image in ImageTexture._cache:
			# Image has already been loaded from disk, recall it from the cache
			img = ImageTexture._cache[image]
		else:
			# Load the image data from disk
			img = texture.ImageFFmpeg(image)
			img.scale = False
			img.flip = False
			if self._caching:
				ImageTexture._cache[image] = img

		data = img.image
		if data is None:
			self.valid = False
			#print("Unable to load the image", image)
			return

		# Upload the texture data
		self.bind()
		glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, img.size[0], img.size[1], 0,
						GL_RGBA, GL_UNSIGNED_BYTE, data)

		self.size = img.size[:]

		self.path = image

		img = None