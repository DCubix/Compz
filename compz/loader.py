# -*- coding: utf-8 -*-
from bge import logic
import json

from .icon import *
from .label import *
from .button import *
from .entry import *
from .layout_base import *
from .linear_layout import *
from .grid_layout import *
from .slider import *
from .panel import *
from .image import *
from .checkbox import *
from .radio_group import *
from .radio import *
from .list import *
from .colorpicker import *

from collections import OrderedDict


class Loader:

	def __init__(self, sys, filePath=None):
		self.system = sys
		self.data = {}
		if filePath is not None:
			with open(filePath) as f:
				self.data = json.load(f, object_pairs_hook=OrderedDict)
			self._load()

		self.comps = OrderedDict()
		self.styles = {}
		self.globalStyle = None
		self.globalForeColor = (1, 1, 1, 1)

	def fromString(self, s):
		self.data = json.loads(s, object_pairs_hook=OrderedDict)
		self._load()

	def _load(self):
		self.comps = {}
		self.styles = {}
		self._parseStyles()
		self._parseSettings()
		self._parseComponentList()

	def _parseComponentList(self):
		if not isinstance(self.data, dict):
			return
		if not "components" in self.data:
			return
		comps = self.data["components"]
		for k, v in list(comps.items()):
			self._parseComponent(k, v)

	def _parseStyles(self):
		if not isinstance(self.data, dict):
			return
		if not "styles" in self.data:
			return
		styles = self.data["styles"]
		for k, v in list(styles.items()):
			self._parseStyle(k, v)

	def _parseSettings(self):
		if not isinstance(self.data, dict):
			return
		if not "settings" in self.data:
			return
		sets = self.data["settings"]
		if "textColor" in sets:
			self.globalForeColor = sets["textColor"]
		if "style" in sets:
			self.globalStyle = self.styles[sets["style"]]
			self.system.style = self.globalStyle

	def _parseComponent(self, name, data):
		keys = list(data.keys())
		if not isinstance(data, dict):
			print("\"data\" must be a dict.")
			return None
		if not "type" in keys:
			print("\"type\" descriptor doesn't exist.")
			return None
		_type = data["type"].lower()

		# Default values
		position = [0, 0]
		size = [20, 20]
		margin = [0, 0]
		row = 0
		col = 0
		rowSpan = 1
		colSpan = 1
		parent = None
		style = None
		visible = True
		enabled = True
		textColor = None

		if "position" in keys:
			position = data["position"]
		if "size" in keys:
			size = data["size"]
		if "parent" in keys:
			parent = data["parent"]
		if "style" in keys:
			style = self.styles[data["style"]]
		if "visible" in keys:
			visible = data["visible"]
		if "enabled" in keys:
			enabled = data["enabled"]
		if "row" in keys:
			row = data["row"]
		if "col" in keys:
			col = data["col"]
		if "rowSpan" in keys:
			rowSpan = data["rowSpan"]
		if "colSpan" in keys:
			colSpan = data["colSpan"]
		if "margin" in keys:
			margin = data["margin"]
		if "textColor" in keys:
			textColor = tuple(data["textColor"])

		comp = None
		if _type == "panel":
			fit = False
			layout = None
			if "fit" in keys:
				fit = data["fit"]
			if "layout" in keys:
				layout = self._parseLayout(data["layout"])
			comp = Panel()
			comp.fit = fit
			comp.layout = layout
		elif _type == "label":
			text = ""
			align = TEXT_ALIGN_LEFT
			if "text" in keys:
				text = data["text"]
			if "alignment" in keys:
				alg = data["alignment"]
				if alg == "TEXT_ALIGN_LEFT":
					align = TEXT_ALIGN_LEFT
				elif alg == "TEXT_ALIGN_CENTER":
					align = TEXT_ALIGN_CENTER
				elif alg == "TEXT_ALIGN_RIGHT":
					align = TEXT_ALIGN_RIGHT
			comp = Label()
			comp.text = text
			comp.textAlignment = align
		elif _type == "button":
			text = ""
			icon = None
			if "text" in keys:
				text = data["text"]
			if "icon" in keys:
				dat = data["icon"]
				img = None
				siz = [16, 16]
				align = ICON_ALIGN_LEFT
				if "image" in dat:
					img = logic.expandPath(dat["image"])
				if "size" in dat:
					siz = dat["size"]
				if "alignment" in dat:
					alg = dat["alignment"]
					if alg == "ICON_ALIGN_LEFT":
						align = ICON_ALIGN_LEFT
					elif alg == "ICON_ALIGN_CENTER":
						align = ICON_ALIGN_CENTER
					elif alg == "ICON_ALIGN_RIGHT":
						align = ICON_ALIGN_RIGHT
				icon = Icon(img, siz)
				icon.alignment = align
			comp = Button()
			comp.text = text
			comp.icon = icon
		elif _type == "slider":
			_min = 0
			_max = 1
			value = 0
			precision = 1
			if "min" in keys:
				_min = data["min"]
			if "max" in keys:
				_max = data["max"]
			if "value" in keys:
				value = data["value"]
			if "precision" in keys:
				precision = data["precision"]
			comp = Slider()
			comp.minimum = _min
			comp.maximum = _max
			comp.value = value
			comp.precision = precision
		elif _type == "check" or _type == "checkbox":
			selected = False
			text = ""
			if "selected" in keys:
				selected = data["selected"]
			if "text" in keys:
				text = data["text"]
			comp = CheckBox()
			comp.selected = selected
			comp.text = text
		elif _type == "radio" or _type == "radiogroup":
			selected = -1
			options = []
			if "selected" in keys:
				selected = data["selected"]
			if "options" in keys:
				options = data["options"]
			comp = self.system.addComp(RadioGroup())
			for opt in options:
				comp.addOption(opt)
			comp.selectedIndex = selected
		elif _type == "entry" or _type == "text" or _type == "textbox":
			text = ""
			readOnly = False
			masked = False
			if "text" in keys:
				text = data["text"]
			if "readOnly" in keys:
				readOnly = data["readOnly"]
			if "masked" in keys:
				masked = data["masked"]
			comp = Entry()
			comp.text = text
			comp.readOnly = readOnly
			comp.masked = masked
		elif _type == "image":
			img = ""
			scale = IMG_SCALE_FIT
			if "path" in keys:
				img = logic.expandPath(data["path"])
			if "scaleMode" in keys:
				scl = data["scaleMode"]
				if scl == "IMG_SCALE_FIT":
					scale = IMG_SCALE_FIT
				elif scl == "IMG_SCALE_STRETCH":
					scale = IMG_SCALE_STRETCH
				elif scl == "IMG_SCALE_NONE":
					scale = IMG_SCALE_NONE
			comp = Image(path=img)
			comp.scaleMode = scale
		elif _type == "list" or _type == "listbox":
			selected = -1
			itemH = 18
			items = []
			if "selected" in keys:
				selected = data["selected"]
			if "items" in keys:
				items = data["items"]
			if "itemHeight" in keys:
				itemH = data["itemHeight"]
			comp = List()
			comp.itemHeight = itemH
			comp.items = items
			comp.selectedIndex = selected
		elif _type == "color" or _type == "colorpicker":
			color = (1, 1, 1)
			h = 0
			s = 0
			v = 1
			if "color" in keys:
				color = tuple(data["color"])
			if "hue" in keys:
				h = data["hue"]
			if "saturation" in keys:
				s = data["saturation"]
			if "value" in keys:
				v = data["value"]
			comp = ColorPicker()
			comp.color = color
			comp.hue = h
			comp.saturation = s
			comp.value = v

		self.system.addComp(comp)

		comp.position = position
		comp.width = size[0]
		comp.height = size[1]
		comp.margin = margin
		comp.row = row
		comp.column = col
		comp.rowSpan = rowSpan
		comp.columnSpan = colSpan
		comp.enabled = enabled
		comp.visible = visible
		if textColor is not None:
			comp.foreColor = textColor
		else:
			comp.foreColor = self.globalForeColor
		if style is not None:
			comp.style = style
		else:
			comp.style = self.globalStyle
		comp.name = name

		if parent is not None:
			_parent = self.comps[parent]
			_parent.addComp(comp)
		self.comps[name] = comp

	def _parseStyle(self, name, data):
		keys = list(data.keys())
		if not isinstance(data, dict):
			print("\"data\" must be a dict.")
			return None

		skin = None
		font = None

		if "skin" in keys:
			skin = logic.expandPath(data["skin"])
		if "font" in keys:
			font = logic.expandPath(data["font"])

		self.styles[name] = Style(skin, font)

	def _parseLayout(self, data):
		keys = list(data.keys())
		if not isinstance(data, dict):
			print("\"data\" must be a dict.")
			return LinearLayout()
		if not "type" in keys:
			print("\"type\" descriptor doesn't exist.")
			return LinearLayout()
		_type = data["type"]

		orientation = ITEM_ORI_VERTICAL
		spacing = 4
		padding = 4
		rows = 2
		cols = 2

		if "orientation" in keys:
			ori = data["orientation"]
			if ori == "ITEM_ORI_VERTICAL":
				orientation = ITEM_ORI_VERTICAL
			elif ori == "ITEM_ORI_HORIZONTAL":
				orientation = ITEM_ORI_HORIZONTAL
		if "spacing" in keys:
			spacing = data["spacing"]
		if "padding" in keys:
			padding = data["padding"]
		if "rows" in keys:
			rows = data["rows"]
		if "cols" in keys:
			cols = data["cols"]

		layout = None
		if _type == "Linear":
			layout = LinearLayout()
			layout.orientation = orientation
		elif _type == "Grid":
			layout = GridLayout()
			layout.rows = rows
			layout.columns = cols
		layout.padding = padding
		layout.spacing = spacing

		return layout
