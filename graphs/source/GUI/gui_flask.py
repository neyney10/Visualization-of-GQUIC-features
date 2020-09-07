from ..coloring_methods import ColorByDefault, ColorByIP, ColorByTime
from flask import Flask, render_template
from flask.json import jsonify
from flask_socketio import SocketIO # https://flask-socketio.readthedocs.io/en/latest/
import os
from numpy.lib.shape_base import column_stack
import pandas as pd
from ..sessions import getSessions
from ..plot_by import plotBy
'''
# install flask, eventlet, flask-socketio
follow these commands:
    set FLASK_ENV=development
    set FLASK_APP=<this-file's-name>
Make sure that you run the following command while inside this directory.
    flask run
'''

def create_app(test_config=None):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret!'

    return app


app = create_app()
socketio = SocketIO(app)

# constants
DATA_DIR = 'source/GUI/data/'

# global variables (for now, until we encapsulate everything in class)
dataFile = None
sessions = None

# routes
@app.route('/')
def index():
    return render_template("index.html")



# socketIO handlers
@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))
    
    directory = os.fsencode(DATA_DIR)
    csvFilenames = []

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".csv"): 
                print("[...Found file: "+ filename + "]")
                csvFilenames.append(filename)
        else:
            continue
    
    socketio.emit('available-data-files', {"data": csvFilenames})

@socketio.on('get-file-columns')
def handle_file_preview(json):
    print('[file data] received json: ' + str(json))
    
    dataFile = pd.read_csv(DATA_DIR + json['data'], nrows=json['nrows']) # nrows=0 -> dont read rows, only extract columns.

    socketio.emit('res-file-columns', {'columns': list(dataFile.columns), 
                                        'data': dataFile.fillna('<no-value>').values.tolist()})

@socketio.on('load-file')
def handle_load_file(json):
    print('[load] received json: ' + str(json))
    
    global dataFile
    dataFile = pd.read_csv(DATA_DIR + json['data'])
    
    socketio.emit('res-load-file', {'res': "Loaded", 'rows': len(dataFile.index)})


@socketio.on('get-sessions')
def handle_sessions(json):
    print('[Sessions] received json: ' + str(json))
    global sessions
    sessions = getSessions(dataFile)
    print(len(sessions))
    socketio.emit('res-sessions', {'sessionIds': list(sessions[:,0]) })

@socketio.on('plot-features')
def handle_plot_features(json):
    print('[plot] received json: ' + str(json))

    featuresToPlot = json['features']
    coloringMethodStr = json['coloringMethod']
    coloringMethodValues = json['coloringMethodValues']
    coloringMethod = None
    if coloringMethodStr == 'IP':
        coloringMethod = ColorByIP(coloringMethodValues)
    elif coloringMethodStr == 'Time':
        coloringMethod = ColorByTime(coloringMethodValues)
    else:
        coloringMethod = ColorByDefault()

    global dataFile
    plotBy(dataFile, featuresToPlot, coloringMethod)



socketio.run(app)