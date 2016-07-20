Label
=================================

.. module:: compz

base: :class:`~compz.Component`

.. class:: Label([text="Label"])

	Simple text display
	
	:arg text: Initial text
	:type text: int
	
	.. attribute:: text
	
		The button text
		
		:type: str
	
	.. attribute:: textAlignmend
	
		Text horizontal alignment
		
		:type: one of :data:`TEXT_ALIGN_LEFT`, :data:`TEXT_ALIGN_RIGHT`, :data:`TEXT_ALIGN_CENTER`

Constants
---------

.. data:: TEXT_ALIGN_LEFT
.. data:: TEXT_ALIGN_RIGHT
.. data:: TEXT_ALIGN_CENTER