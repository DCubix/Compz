# -*- coding: utf-8 -*-
from bgl import *
from bge import render, logic, events

_glGenTextures = glGenTextures


def glGenTexture():
	id_buf = Buffer(GL_INT, 1)
	_glGenTextures(1, id_buf)
	return id_buf.to_list()[0]


_glDeleteTextures = glDeleteTextures


def glDeleteTextures(textures):
	n = len(textures)
	id_buf = Buffer(GL_INT, n, textures)
	_glDeleteTextures(n, id_buf)


_glGetIntegerv = glGetIntegerv


def glGetIntegerv(pname):
	buf = Buffer(GL_INT, 4)
	_glGetIntegerv(pname, buf)
	return buf.to_list()


def glGenBuffer():
	id_buf = Buffer(GL_INT, 1)
	glGenBuffers(1, id_buf)
	return id_buf.to_list()[0]


_glDeleteBuffers = glDeleteBuffers


def glDeleteBuffers(bufs):
	n = len(bufs)
	id_buf = Buffer(GL_INT, n, bufs)
	_glDeleteBuffers(n, id_buf)


def glGenVertexArray():
	id_vao = Buffer(GL_INT, 1)
	glGenVertexArrays(1, id_vao)
	return id_vao.to_list()[0]


_glDeleteVertexArrays = glDeleteVertexArrays


def glDeleteVertexArrays(vaos):
	n = len(vaos)
	id_buf = Buffer(GL_INT, n, vaos)
	_glDeleteVertexArrays(n, id_buf)


def GFX_mousePosition():
	w = render.getWindowWidth()
	h = render.getWindowHeight()
	return [int(w * logic.mouse.position[0]), int(h * logic.mouse.position[1])]


def GFX_mouseClick(button):
	return logic.mouse.events[button] == logic.KX_INPUT_JUST_ACTIVATED


def GFX_mouseDown(button):
	return logic.mouse.events[button] == logic.KX_INPUT_ACTIVE


def GFX_mouseRelease(button):
	return logic.mouse.events[button] == logic.KX_INPUT_JUST_RELEASED


def GFX_keyDown(btn, state=logic.KX_INPUT_ACTIVE):
	return logic.keyboard.events[btn] == state


def GFX_keyPressed(btn, state=logic.KX_INPUT_JUST_ACTIVATED):
	return logic.keyboard.events[btn] == state


def GFX_keyReleased(btn, state=logic.KX_INPUT_JUST_RELEASED):
	return logic.keyboard.events[btn] == state


def GFX_getAllKeys():
	keys = {}
	for k, v in events.__dict__.items():
		if not k.startswith("__"):
			if k not in ["EventToCharacter", "EventToString",
							"RETKEY", "WHEELUPMOUSE",
							"WHEELDOWNMOUSE", "MOUSEY", "MOUSEX",
							"LEFTMOUSE", "MIDDLEMOUSE", "RIGHTMOUSE"]:
				keys[k] = v
	return keys

GFX_SupportedKeys = GFX_getAllKeys()


class GFXbase:
	sbox = [0, 0, 1, 1]
	on = False

	def set2D(self):
		width = render.getWindowWidth()
		height = render.getWindowHeight()

		glDisable(GL_CULL_FACE)
		glDisable(GL_LIGHTING)
		glDisable(GL_DEPTH_TEST)

		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		gluOrtho2D(0, width, height, 0)
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()

		glHint(GL_POLYGON_SMOOTH_HINT, GL_NICEST)

	def drawQuad(self, x, y, w, h, texture=None, color=(1, 1, 1, 1)):
		pass

	def drawQuadUV(self, x, y, w, h, texture=None,
		uv=(0, 0, 1, 1), color=(1, 1, 1, 1)):
		pass

	def drawWireQuad(self, x, y, w, h, color=(0, 0, 0, 1), lineWidth=1):
		glLineWidth(lineWidth)
		glColor4f(*color)
		glBegin(GL_LINE_LOOP)
		glVertex2f(x, y)
		glVertex2f(x + w, y)
		glVertex2f(x + w, y + h)
		glVertex2f(x, y + h)
		glEnd()
		glLineWidth(1)

	def draw9Patch(self, x, y, w, h, o, s, t=None, col=(1, 1, 1, 1)):
		os = o / s

		# Top left
		self.drawQuadUV(x, y, o, o, t, (0, 0, os, os), col)
		# Top mid
		self.drawQuadUV(x + o, y, w - o * 2, o, t, (os, 0, 1 - os * 2, os), col)
		# Top right
		self.drawQuadUV(x + w - o, y, o, o, t, (1 - os, 0, 1, os), col)
		# Mid left
		self.drawQuadUV(x, y + o, o, h - o * 2, t, (0, os, os, 1 - os), col)
		# Middle
		self.drawQuadUV(x + o, y + o, w - o * 2, h - o * 2, t,
			(os, os, 1 - os, 1 - os), col)
		# Mid right
		self.drawQuadUV(x + w - o, y + o, o, h - o * 2, t,
			(1 - os, os, 1, 1 - os), col)
		# Bottom left
		self.drawQuadUV(x, y + h - o, o, o, t, (0, 1 - os, os, 1), col)
		# Bottom mid
		self.drawQuadUV(x + o, y + h - o, w - o * 2, o, t,
			(os, 1 - os, 1 - os * 2, 1), col)
		# Bottom right
		self.drawQuadUV(x + w - o, y + h - o, o, o, t,
			(1 - os, 1 - os, 1, 1), col)

	def clipBegin(self, x, y, w, h, padding=[0, 0, 0, 0]):
		vp = glGetIntegerv(GL_VIEWPORT)

		B = [
			x + padding[0],
			y + padding[1],
			w - padding[2] * 2,
			h - padding[3] * 2
		]

		# Do some math to invert the coords
		scp = [0, 0, int(B[2]), int(B[3])]
		scp[0] = int(B[0] + vp[0])
		scp[1] = int(vp[1] + (vp[3] - B[1] - B[3]))

		self.on = glIsEnabled(GL_SCISSOR_TEST)
		self.sbox = glGetIntegerv(GL_SCISSOR_BOX)

		glEnable(GL_SCISSOR_TEST)
		glScissor(*scp)

	def clipEnd(self):
		glScissor(*self.sbox)
		if not self.on:
			glDisable(GL_SCISSOR_TEST)


class GFXvbo(GFXbase):

	def __init__(self):
		self.vbo = 0
		self.uv = 0
		self.program = 0

		verts = [
			0, 0, 0,
			0, 1, 0,
			1, 0, 0,
			1, 1, 0,
			1, 0, 0,
			0, 1, 0
		]

		self.vertBuff = Buffer(GL_FLOAT, len(verts), verts)

		self.vbo = glGenBuffer()
		glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
		glBufferData(GL_ARRAY_BUFFER, len(verts) * 4, self.vertBuff, GL_STATIC_DRAW)

		self.uv = glGenBuffer()
		self.setUV(0, 0, 1, 1)

		vsID = glCreateShader(GL_VERTEX_SHADER)
		fsID = glCreateShader(GL_FRAGMENT_SHADER)

		vsCode = """
			varying vec2 out_uv;
			varying vec4 out_color;
			void main() {
				gl_Position = ftransform();
				out_uv = gl_MultiTexCoord0.st;
				out_color = gl_Color;
			}
		"""
		fsCode = """
			uniform sampler2D image;
			uniform int hasImage;
			varying vec2 out_uv;
			varying vec4 out_color;
			void main() {
				if (hasImage == 1) {
					gl_FragColor = texture2D(image, out_uv) * out_color;
				} else {
					gl_FragColor = out_color;
				}
			}
		"""

		glShaderSource(vsID, vsCode)
		glCompileShader(vsID)

		glShaderSource(fsID, fsCode)
		glCompileShader(fsID)

		self.program = glCreateProgram()
		glAttachShader(self.program, vsID)
		glAttachShader(self.program, fsID)
		glLinkProgram(self.program)

		glDeleteShader(vsID)
		glDeleteShader(fsID)

		#glBindBuffer(GL_ARRAY_BUFFER, 0)

	def set2D(self):
		width = render.getWindowWidth()
		height = render.getWindowHeight()

		glDisable(GL_CULL_FACE)
		glDisable(GL_LIGHTING)
		glDisable(GL_DEPTH_TEST)

		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		gluOrtho2D(0, width, height, 0)
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()

	def setUV(self, uvx1, uvy1, uvx2, uvy2):
		uvs = [
			uvx1, uvy1,
			uvx1, uvy2,
			uvx2, uvy1,
			uvx2, uvy2,
			uvx2, uvy1,
			uvx1, uvy2
		]
		self.uvBuff = Buffer(GL_FLOAT, len(uvs), uvs)

		glBindBuffer(GL_ARRAY_BUFFER, self.uv)
		glBufferData(GL_ARRAY_BUFFER, len(uvs) * 4, self.uvBuff, GL_STATIC_DRAW)
		glBindBuffer(GL_ARRAY_BUFFER, 0)

	def drawQuad(self, x, y, w, h, texture=None, color=(1, 1, 1, 1)):
		glEnable(GL_BLEND)
		glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

		glColor4f(*color)

		glPushMatrix()

		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()
		glTranslatef(x, y, 0.0)
		glScalef(w, h, 1.0)

		glUseProgram(self.program)

		imageLOC = glGetUniformLocation(self.program, "image")
		hasimageLOC = glGetUniformLocation(self.program, "hasImage")

		if texture is not None:
			texture.bind(0)
			glUniform1i(imageLOC, 0)
			glUniform1i(hasimageLOC, 1)
		else:
			glUniform1i(hasimageLOC, 0)

		glEnableClientState(GL_VERTEX_ARRAY)
		glVertexPointer(3, GL_FLOAT, 0, self.vertBuff)
		glEnableClientState(GL_TEXTURE_COORD_ARRAY)
		glTexCoordPointer(2, GL_FLOAT, 0, self.uvBuff)

		glDrawArrays(GL_TRIANGLES, 0, 6)

		glDisableClientState(GL_VERTEX_ARRAY)
		glDisableClientState(GL_TEXTURE_COORD_ARRAY)

		glPopMatrix()

		glBindBuffer(GL_ARRAY_BUFFER, 0)
		glUseProgram(0)

		glDisable(GL_BLEND)

	def drawQuadUV(self, x, y, w, h, texture=None, uv=(0, 0, 1, 1),
		color=(1, 1, 1, 1)):
		self.setUV(*uv)
		self.drawQuad(x, y, w, h, texture, color)
		self.setUV(0, 0, 1, 1)

	def __del__(self):
		glDeleteBuffers([self.vbo, self.uv, self.ibo])
		glDeleteProgram(self.program)