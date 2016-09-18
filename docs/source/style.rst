Style
=================================

.. module:: compz

.. class:: Style([skinPath=None, fontPath=None])

	Style class for image skinning
	
	:arg skinPath: Skin texture path
	:type skinPath: str
	:arg fontPath: Font path
	:type fontPath: str
	
	.. attribute:: skin
	
		Skin texture
		
		:type: :class:`~compz.ImageTexture`
	
	.. attribute:: font
	
		Font face
		
		:type: :class:`~compz.Font`
	
	.. attribute:: offset
	
		9-Patch offset
		
		:type: int
		:default: 4
