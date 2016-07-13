# -*- coding: utf-8 -*-
from bge import logic


class Timer:

	def __init__(self):
		self.enabled = True
		self.time = 0.0
		self.delay = 0.0

	def reset(self):
		self.time = 0.0

	def update(self):
		if self.enabled:
			self.time += (1.0 / logic.getLogicTicRate()) * (self.delay + 1.0)