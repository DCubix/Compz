Rect
=================================

.. module:: compz

.. class:: Rect([x=0, y=0, width=1, height=1])

	:arg x: X position
	:type x: int
	:arg y: Y position
	:type y: int
	:arg width: Width
	:type width: int
	:arg height: Height position
	:type height: int
	
	.. attribute:: x
	
		X position
		
		:type: int

	.. attribute:: y
	
		Y position
		
		:type: int

	.. attribute:: width
	
		Width
		
		:type: int

	.. attribute:: height
	
		Height
		
		:type: int

	.. method:: hasPoint(x, y)
	
		Checks if there's a point inside this rect
		
		:arg x: X
		:type x: int
		:arg y: Y
		:type y: int
		
		:return: True if the point is inside this rect
		:rtype: bool
