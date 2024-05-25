import eventlet
import socketio

sio = socketio.Server(cors_allowed_origins=['http://localhost:4200'])
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})

@sio.event
def connect(sid, environ):
    print('#### connect ', sid)

# @sio.event
# def my_message(sid, data):
#     print('### message:', data)
#     sio.broadcast.emit('received', {data: data, 'message': 'Message sent to server.'})

@sio.event
def disconnect(sid):
    print('####  disconnect ', sid)

@sio.on('message', namespace='*')
def my_event_any_namespace(namespace, sid, data):
    print('### message:', data)
    sio.emit('received', {'data': data, 'message': 'Message sent to server.'})


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 4000)), app)