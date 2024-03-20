<<<<<<< HEAD
from flask import Flask, render_template,request, send_from_directory,redirect,url_for,make_response
from authentication import extract_credentials,validate_password
=======
from flask import Flask, render_template,request, send_from_directory,redirect,url_for,make_response,request
from authentication import extract_credentials,validate_password,extract_credentialslogin
>>>>>>> 69212b900face746f36aebb438e1a425d05d96fd
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
    print("hello")
    auth_token = request.cookies.get("auth_token")

    # checks if user is logged in
    if auth_token:
        log = True
    else:
        log = False

    return render_template("index.html", content_type='text/html', logged_in=log)

#takes the user to the register form
@app.route("/register")
def registerPath():
    return render_template('register.html', content_type='text/html')

#takes the user to the login form
@app.route("/login")
def loginPath():
    return render_template('login.html', content_type='text/html')

# Register user
@app.route('/auth-register', methods=['POST'])
def register():
    username, password1, password2 = extract_credentials(request)
    if password1 != password2:
        return "The entered passwords do not match"
    
    if not validate_password(password1):
        return 'Password does not meet the requirements'
    
    user = db.accounts.find_one({'username': username})
    if user:
        return "Username is taken"
    
    # Generate a salt
    salt = bcrypt.gensalt()
    
    # Hash the password with the salt
    hashed_password = bcrypt.hashpw(password1.encode('utf-8'), salt)
    
    # Store the username, hashed password, and salt in the database
    data = {"username": username, "hash": hashed_password, "salt": salt,"password":password1}
    db.accounts.insert_one(data)
    
    return redirect(url_for('loginPath'))

@app.route('/auth-login', methods=['POST'])
def login():
    username, password = extract_credentialslogin(request)

    # Retrieve user from database
    user = db.accounts.find_one({'username': username})

    if user:
        salt = user['salt']
        hash = bcrypt.hashpw(password.encode('utf-8'),salt)

        if(hash == user["hash"]):
            token = secrets.token_hex(16)
            hashed_token = hashlib.sha256(token.encode()).hexdigest()
            db.accounts.update_one({'username':username},{'$set':{'token':hashed_token}})


            # Create a response object
            resp = make_response(redirect('/'))  # Redirect to the homepage

            # Set the token as a cookie
            resp.set_cookie('auth_token', token, httponly=True, max_age=3600)  # Expires in 1 hour

            return resp

    return {'message': 'Invalid username or password'}, 401


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
