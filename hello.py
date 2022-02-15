from flask import Flask, render_template
from flask import Flask, jsonify, request, url_for
from flask_jsglue import JSGlue

app = Flask(__name__)
JSGlue(app)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

@app.route('/')
def index():
   return render_template('/index.html')
if __name__ == '__main__':
   app.run()