Image
=================================

.. module:: compz

base: :class:`~compz.Component`

.. class:: Image([path="", style=None])

	Image/Texture viewer
	
	.. attribute:: texture
	
		Texture to be displayed
		
		:type: :class:`~compz.ImageTexture`
	
	.. attribute:: scaleMode
	
		Texture scaling mode
		
		:type: int, one of :data:`IMG_SCALE_FIT`, :data:`IMG_SCALE_STRETCH`, :data:`IMG_SCALE_NONE`
	
Constants
---------

.. data:: IMG_SCALE_FIT
.. data:: IMG_SCALE_STRETCH
.. data:: IMG_SCALE_NONE