Component
=================================

.. module:: compz

.. class:: Component([style=None])

	The base class of everything.
	
	:arg style: Style instance for image skinning
	:type style: :class:`~compz.Style`

	.. attribute:: bounds
	
		Component bounds rectangle
		
		:type: :class:`~compz.Rect`
	
	.. attribute:: parent
		
		Parent component
		
		:type: :class:`~compz.Component`

	.. attribute:: backColor
	
		Background color
		
		:type: tuple
	
	.. attribute:: foreColor
	
		Foreground color. Used for text
		
		:type: tuple
	
	.. attribute:: system
	
		Main GUI system
		
		:type: :class:`~compz.Compz`
	
	.. attribute:: events
	
		Event handler
		
		:type: :class:`~compz.Event`
		
	.. attribute:: state
	
		Component state
		
		:type: one of :data:`COMP_STATE_NORMAL`, :data:`COMP_STATE_HOVER`, :data:`COMP_STATE_CLICK`, :data:`COMP_STATE_INACTIVE`
	
	.. attribute:: style
	
		Component style instance
		
		:type: :class:`~compz.Style`
	
	.. attribute:: visible
	
		Component visibility state
		
		:type: bool
	
	.. attribute:: enabled
	
		Component event handling enabled state
		
		:type: bool
	
	.. attribute:: row
	
		Row index (for :class:`~compz.GridLayout` only)
		
		:type: int
		:default: 0
	
	.. attribute:: column
	
		Column index (for :class:`~compz.GridLayout` only)
		
		:type: int
		:default: 0
	
	.. attribute:: rowSpan
	
		Row span count (for :class:`~compz.GridLayout` only)
		
		:type: int
		:default: 1
	
	.. attribute:: columnSpan
	
		Column span count (for :class:`~compz.GridLayout` only)
		
		:type: int
		:default: 1
		
	.. attribute:: drawBackground
	
		Enable/Disabl background drawing
		
		:type: bool
	
	.. attribute:: position
	
		Component position
		
		:type: list or :class:`~compz.Point`
		
	.. attribute:: x
		
		Component X position
		
		:type: int
	
	.. attribute:: y
		
		Component Y position
		
		:type: int
	
	.. attribute:: width
		
		Component width
		
		:type: int
	
	.. attribute:: height
	
		Component height
		
		:type: int
	
	.. method:: transformedBounds()
	
		Gets the transformed bounds rectangle based on parent
		
		:return: the transformed bounds
		:rtype: :class:`~compz.Rect`
	
	.. method:: centerOnScreen(vertical=True, horizontal=True)
	
		Set the component position to the center of the screen

		:arg vertical: Center vertically
		:type vertical: bool
		:arg horizontal: Center horizontally
		:type horizontal: bool
	
	.. method:: event
	
		Event processing method called after :meth:`update`
	
	.. method:: update
	
		Update logic method
	
	.. method:: draw
	
		Drawing method
	
Constants
---------

.. data:: COMP_STATE_NORMAL
.. data:: COMP_STATE_HOVER
.. data:: COMP_STATE_CLICK
.. data:: COMP_STATE_INACTIVE
.. data:: COMP_STATE_CUSTOM
