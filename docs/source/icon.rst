Icon
=================================

.. module:: compz

.. class:: Icon(path[, size=[16, 16]])

	Simple icon class for Buttons
	
	:arg path: Texture/Icon path
	:type path: str
	:arg size: Icon size
	:type size: list of 2 ints
	
	.. attribute:: texture
	
		Image texture for the icon
		
		:type: :class:`~compz.ImageTexture`
	
	.. attribute:: size
	
		Icon size
		
		:type: list of 2 ints
	
	.. attribute:: alignment
	
		Icon alignment
		
		:type: int, one of :data:`ICON_ALIGN_LEFT`, :data:`ICON_ALIGN_RIGHT`, :data:`ICON_ALIGN_CENTER`

Constants
---------	

.. data:: ICON_ALIGN_LEFT
.. data:: ICON_ALIGN_RIGHT
.. data:: ICON_ALIGN_CENTER