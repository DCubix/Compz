Point
=================================

.. module:: compz

.. class:: Point([x=0, y=0])

	Basic point class
	
	:arg x: X position
	:type x: int
	:arg y: Y position
	:type y: int
	
	.. method:: distance(p)
	
		Get the distance between this and ``p``
		
		:arg p: The other point
		:type p: :class:`~compz.Point`
		:return: The distance between this and ``p`` in pixels
		:rtype: float