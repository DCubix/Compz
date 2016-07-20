Radio
=================================

.. module:: compz

base: :class:`~compz.CheckBox`

.. class:: Radio([text="CheckBox", style=None])

	Radio button/single choice (acts like multiple choice when there's no group assigned)
	
	:arg text: Initial text
	:type text: int
	:arg style: Component style
	:type style: :class:`~compz.Style`
	
	.. attribute:: group
	
		Radio group
		
		:type: :class:`~compz.RadioGroup`