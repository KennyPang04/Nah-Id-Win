from flask import Flask, render_template,request, send_from_directory,redirect,url_for
from authentication import extract_credentials,validate_password
from pymongo import MongoClient
from db import db
import bcrypt
import hashlib
import secrets

app = Flask(__name__)

@app.after_request
def add_header(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    return response

@app.route('/')
def index():
    return render_template("index.html", content_type='text/html')

@app.route('/auth-register', methods=['POST'])
def register():
    username,password1,password2 = extract_credentials(request)
    if password1 != password2:
        "The entered password's do not match"
    
    if not validate_password(password1):
        return 'Password does not meet the requirements'
    
    user = db.accounts.find_one({'username':username})
    if user:
        return "Username is taken"
    
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(password1.encode('utf-8'),salt)
    data = {"username":username,"salt":salt,"hash":hash}
    db.accounts.insert_one(data)
    return redirect(url_for('login'))

@app.route('/auth-login',methods=['POST'])
def login():
    username = request.form('username')
    password = request.form('password')

    user = db.accounts.find_one({'username':username})
    if user == None:
        return "username not found"

    else:
        salt = user["salt"]
        


    return redirect(url_for('/'))








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
