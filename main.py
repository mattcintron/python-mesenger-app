#build simple messenger app - in flask -
#refernce code here - 
# https://codeburst.io/building-your-first-chat-application-using-flask-in-7-minutes-f98de4adfa5d


#lets start by importing flask - 
from flask import Flask
from flask import render_template, url_for, flash, redirect, request, Response
# next lets import socket io
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jnkdjnfjknfl1232#'
socketio = SocketIO(app)



@app.route('/')
def sessions():
    return render_template('session.html')

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)





if __name__ == '__main__':
    socketio.run(app, debug=True)







