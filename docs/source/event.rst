Event
=================================

.. module:: compz

.. class:: Event

	Event handler
	
	.. attribute:: events
	
		Event handlers
		
		:type: dict
	
	.. method:: set(event, callback)
	
		Set event callback
	
		:arg event: Event code
		:type event: int, one of :data:`EV_MOUSE_CLICK`, :data:`EV_MOUSE_RELEASE`, :data:`EV_MOUSE_ENTER`,
								 :data:`EV_MOUSE_LEAVE`, :data:`EV_KEY_PRESS`, :data:`EV_KEY_RELEASE`,
								 :data:`EV_KEY_DOWN`
		:arg callback: Event callback
		:type callback: function
	
	.. method:: call(event, *args)
		
		Call the specified event
		
		:arg event: Event code
		:type event: int, one of :data:`EV_MOUSE_CLICK`, :data:`EV_MOUSE_RELEASE`, :data:`EV_MOUSE_ENTER`,
								 :data:`EV_MOUSE_LEAVE`, :data:`EV_KEY_PRESS`, :data:`EV_KEY_RELEASE`,
								 :data:`EV_KEY_DOWN`
		
		:arg args: Arguments
		:type args: Argument list
		
	.. method:: register(event)
	
		Register an event code to the event list
		
		:arg event: Event code
		:type event: int

Constants
---------

.. data:: EV_MOUSE_CLICK
.. data:: EV_MOUSE_RELEASE
.. data:: EV_MOUSE_ENTER
.. data:: EV_MOUSE_LEAVE
.. data:: EV_KEY_PRESS
.. data:: EV_KEY_RELEASE
.. data:: EV_KEY_DOWN