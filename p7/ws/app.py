from flask_socketio import SocketIO, emit, Namespace, join_room, leave_room
from flask import session


class RoomAction(Namespace):
	def on_connect(self):
		join_room('1')
		print(session['user'])

	def on_disconnect(self):
		print('Client disconnected')

	def on_change_room(self, data):
		room = data.get('room')
		unsub_room = data.get('unsub_room')
		leave_room(unsub_room)
		join_room(room)

	def on_my_event(self, data):
		print(session['user'])
		print('on my')
		if room := data.get('room'):
			# save

			# not get
			emit('recv', data, broadcast=True, to=room)


class MyWebSocket(SocketIO):
	def __init__(self, app, **kwargs):
		super().__init__(app, **kwargs)
		self.on_namespace(RoomAction())


