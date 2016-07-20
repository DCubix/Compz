Font
=================================

.. module:: compz

.. class:: Font([path=None])

	Simple font class based on BLF
	
	:arg path: Font path
	:type path: int
	
	.. attribute:: id
	
		Font ID
		
		:type: int
	
	.. attribute:: size
	
		Font size (points)
		
		:type: float
	
	.. attribute:: shadowed
	
		Enable/Disable font shadow
		
		:type: bool
		
	.. attribute:: shadow_offset
	
		Shadow offset
		
		:type: list of 2 floats
	
	.. method:: measure(text)
		
		Get font metrics of the specified text
		
		:arg text: Text to measure
		:type text: str
		:return: Text size
		:rtype: list of 2 floats
	
	.. method:: draw(text, x, y)
	
		Draws the specified text
		
		:arg text: Text to draw
		:type text: str
		:arg x: X position
		:type x: int
		:arg y: Y position
		:type y: int