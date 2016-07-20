Entry
=================================

.. module:: compz

base: :class:`~compz.Component`

.. class:: Entry([text=""], [style=None])

	Advanced text input
	
	:arg text: Initial text
	:type text: int
	:arg style: Component style
	:type style: :class:`~compz.Style`
	
	.. attribute:: text
	
		Text data
		
		:type: str
	
	.. attribute:: readOnly
	
		Lock/Unlock text input
		
		:type: bool
	
	.. attribute:: masked
	
		Hide/Unhide text data
		
		:type: bool