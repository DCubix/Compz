ImageTexture
=================================

.. module:: compz

.. class:: ImageTexture(image[, interp_mode=GL_NEAREST, caching=True])
	
	Simple texture class
	
	:arg image: Image path
	:type image: str
	:arg interp_mode: Interpolation mode
	:type interp_mode: int
	:arg caching: Cache this image (prevent from loading the same image multiple times)
	:type caching: bool
	
	.. attribute:: size
	
		Image size
		
		:type: list of 2 ints
	
	.. attribute:: interp_mode
	
		Get/Set interpolation mode
		
		:type: int, one of :data:`~bgl.GL_NEAREST`, :data:`~bgl.GL_LINEAR`
	
	.. method:: reload(image)
	
		Reloads this imaage only if the image is different
		
		:arg image: Image path
		:type image: str