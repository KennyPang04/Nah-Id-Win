from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.after_request
def add_header(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    return response

@app.route('/')
def index():
    return render_template("index.html", content_type='text/html')

@app.route('/login')
def login():
    return render_template("login.html", content_type='text/html')

@app.route('/static/js/<path:filename>')
def js(filename):   
    return send_from_directory('static/js', filename, mimetype='text/javascript')

@app.route('/static/css/<path:filename>')
def css(filename):
    return send_from_directory('static/css', filename, mimetype='text/css')

@app.route('/static/image/<path:filename>')
def img(filename):
    return send_from_directory('static/image', filename, mimetype='image/png')




if __name__ == __name__:
    app.run(debug=True, host='0.0.0.0', port=8080)
