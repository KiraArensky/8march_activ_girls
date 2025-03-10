from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)


# Main index.html template
@app.route('/')
def index():
    return render_template('index.html')


# Personal greeting pages
@app.route('/personal/<name>.html')
def personal_greeting(name):
    return render_template(f'personal/{name}.html')


# Serve static images
@app.route('/pic/<filename>')
def serve_image(filename):
    return send_from_directory('pic', filename)


if __name__ == '__main__':
    app.run(port='5000')
