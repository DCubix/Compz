Layout Base
=================================

.. module:: compz

.. class:: LayoutBase

	Base class for layout managers
	
	.. attribute:: padding
	
		Inner padding in pixels
		
		:type: int
		
	.. attribute:: spacing

		Spacing between components in pixels
		
		:type: int
	
	.. method:: apply(comp)
	
		Applies this layout to a component
		
		:arg comp: Component
		:type comp: :class:`~compz.Component`
	
	.. method: reset()
	
		Resets this layout manager