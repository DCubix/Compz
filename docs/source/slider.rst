Slider
=================================

.. module:: compz

base: :class:`~compz.Component`

.. class:: Slider([_min=0, _max=1, style=None])

	Slider/TrackBar/Value Range
	
	:arg _min: Minimum value
	:type _min: float
	:arg _max: Maximum value
	:type _max: float
	:arg style: Component style
	:type style: :class:`~compz.Style`
	
	.. attribute:: minimum
		
		Minimum value
		
		:type: float

	.. attribute:: maximum
		
		Maximum value
		
		:type: float
		
	.. attribute:: value
	
		Current value
		
		:type: float
	
	.. attribute:: precision
	
		Slider precision (decimal places)
		
		:type: int
	
Constants
---------

.. data:: EV_SLIDER_VALUE_CHANGE