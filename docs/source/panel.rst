Panel
=================================

.. module:: compz

base: :class:`~compz.Component`

.. class:: Panel([style=None])
	
	Panel/Container/Box
	
	:arg style: Component style
	:type style: :class:`~compz.Style`
	
	.. attribute:: children
	
		All the components that are attached to this container/panel
		
		:type: list of :class:`~compz.Component`
	
	.. attribute:: layout
	
		Layout manager
		
		:type: :class:`~compz.LayoutBase`
	
	.. method:: addComp(comp)
	
		Adds a new component to the system
	
		:arg comp: Component to add
		:type comp: :class:`~compz.Component`