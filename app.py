# for connecting flask and index.html file inside template folder

# from flask import Flask, render_template
# from flask_socketio import SocketIO, emit

# app = Flask(__name__)
# socketio = SocketIO(app)

# # Initial data for the object
# object_data = {
#     'name': 'Example Object',
#     'status': 'Online'
# }

# # Route to serve the HTML page
# @app.route('/')
# def index():
#     return render_template('index.html')

# # Route to serve JSON data through WebSocket
# @socketio.on('get_object_data')
# def get_object_data():
#     emit('update_object', object_data)

# @socketio.on('connect')
# def handle_connect():
#     print('Client connected')
#     emit('update_object', object_data)  # Send initial object data to the connected client

# if __name__ == '__main__':
#     socketio.run(app, debug=True)











# for connecting react and flask web socket api

from flask import Flask, jsonify
from flask_socketio import SocketIO, emit
from flask_cors import CORS
import os
# from gevent.pywsgi import WSGIServer


app = Flask(__name__)
# CORS(app, resources={r"/api/*": {"origins": "*"}}) 
# CORS(app, resources={r"/socket.io/*": {"origins": "*"}})
socketio = SocketIO(app, cors_allowed_origins="*")


# Initial data for the object
object_data = {
    'name': 'Example Object',
    'status': 'Online'
}

# Route to serve JSON data
@app.route('/api/object_data', methods=['GET'])
def get_object_data():
    return jsonify(object_data)

@socketio.on('connect')
def handle_connect():
    print('Client connected')
    emit('update_object', object_data)  # Send initial object data to the connected client

if __name__ == '__main__':
    # app.run(host="localhost", port=os.environ.get('PORT'))
    socketio.run(app, debug=False)
    # http_server = WSGIServer(('', 5000), app)
    # http_server.serve_forever()

