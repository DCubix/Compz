RadioGroup
=================================

.. module:: compz

base: :class:`~compz.Panel`

.. class:: RadioGroup([radioStyle=None])

	Radio group panel
	
	:arg radioStyle: Style for the radio buttons
	:type radioStyle: :class:`~compz.Style`
	
	.. attribute:: selectedIndex
	
		Currently selected option index (in insertion order)
		
		:type: int
		:default: -1 (none selected)
	
	.. attribute:: radioStyle
	
		Style for the radio buttons
		
		:type: :class:`~compz.Style`
	
	.. method:: addOption(opt)
	
		Add a new option to the group
		
		:arg opt: Option text
		:type opt: str
		:return: The new radio button
		:rtype: :class:`~compz.Radio`

Constants
---------

.. data:: EV_OPTION_SELECTED