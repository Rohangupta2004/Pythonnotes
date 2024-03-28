"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)"""
from flask import Flask, render_template
import threading
import webview
from drawing_app import main as run_tkinter_app

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def start_tkinter_app():
    run_tkinter_app()

@app.route('/start-app')
def start_app():
    t = threading.Thread(target=start_tkinter_app)
    t.start()
    return 'Starting the Tkinter application...'

if __name__ == '__main__':
    webview.create_window("Embedded Tkinter Drawing App", app=app, width=800, height=600, js_api= True)
    webview.start()