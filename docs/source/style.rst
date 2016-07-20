Style
=================================

.. module:: compz

.. class:: Style([name="Component", stylesPath=None, fontPath=None])

	Style class for image skinning
	
	:arg name: Resource name, the one that comes before the "_"
	:type name: str
	:arg stylesPath: Texture path
	:type stylesPath: str
	:arg fontPath: Font path
	:type fontPath: str
	
	.. attribute:: textures
	
		Textures dictionary
		
		:type: dict. The keys can be one of :data:`COMP_STATE_NORMAL`, :data:`COMP_STATE_HOVER`, :data:`COMP_STATE_CLICK`,
											:data:`COMP_STATE_INACTIVE`, or "custom"
	
	.. attribute:: font
	
		Font face
		
		:type: :class:`~compz.Font`
	
	.. attribute:: offset
	
		9-Patch offset
		
		:type: int
		:default: 4