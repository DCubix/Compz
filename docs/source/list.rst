List
=================================

.. module:: compz

base: :class:`~compz.Component`

.. class:: List([style=None])

	Simple list box component
	
	:arg style: Style instance for image skinning
	:type style: :class:`~compz.Style`

	.. attribute:: items
	
		List items
		
		:type: list of Anything (for custom classes, __repr__ and __str__ must be overridden)
	
	.. attribute:: itemHeight
		
		Height for each list item.
		
		:type: int

	.. attribute:: selectedIndex
	
		Currently selected index.
		
		:type: int