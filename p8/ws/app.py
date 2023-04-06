from flask_socketio import SocketIO, emit, Namespace, join_room, leave_room


class MyCustomAction(Namespace):
	def __init__(self):
		super().__init__()

	def on_connect(self):
		join_room('1')

	def on_disconnect(self):
		print('Client disconnected')

	def on_change_room(self, data):
		room = data.get('room')
		unsub_room = data.get('unsub_room')
		if room and unsub_room:
			print('changed')
			leave_room(unsub_room)
			join_room(room)

	def on_my_event(self, data):
		print('on my')
		if room := data.get('room'):
			emit('recv', data, broadcast=True, to=room)


class MyWebSocket(SocketIO):
	def __init__(self, app):
		super().__init__(app)
		self.on_namespace(MyCustomAction())


