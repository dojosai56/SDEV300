"""Welcome to Python Flask Lab"""
import string
from datetime import datetime
from flask import Flask, render_template, request
from passlib.hash import sha256_crypt

SIGNEDIN_USER = ""

def save_data(username, password):
    '''
    password already validated
    if username isn't in use save user+password to database
    :param username:
    :param password:
    :return: True if user successfully saved in database
    '''
    with open('username_fileDB.txt', 'a+') as file:
        file.seek(0)
        for line in file:
            data = line.strip().split(",")
            if username == data[0]:
                return False  # since username exists
        hash_pass = sha256_crypt.hash(password)
        # write to end of file since username is unique
        file.write(username + "," + hash_pass + "\r")
        return True  # success


def query_user(username, password):
    '''

    :param username:
    :param password:
    :return: False if username/password not correct
    '''
    global SIGNEDIN_USER
    with open('username_fileDB.txt', 'r') as file:
        for line in file:
            data = line.strip().split(",")
            if username == data[0] and sha256_crypt.verify(password, data[1]):
                SIGNEDIN_USER = "Welcome " + username + "!"
                return True  # user/pass exists

        return False

def invalid_password(password):
    '''
    method for detecting invalid passwords
    '''
    is_at_least_one = bool((any(c.isupper() for c in password)) and
                           (any(c.islower() for c in password)) and
                           (any(c.isdigit() for c in password)) and
                           (any(c in string.punctuation for c in password)))

    if len(password) >= 12 and is_at_least_one and not any(c == " " for c in password):
        return False # is not invalid

    return True #is invalid

# Create Flask app load app.config
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    '''
    Home tab
    '''
    current_time = "Time Stamp: " + str(datetime.now())
    return render_template("index.html", timestamp=current_time, signedinas=SIGNEDIN_USER)

@app.route("/about")
def about():
    '''
    About Tab
    '''
    current_time = "Time Stamp: " + str(datetime.now())
    return render_template("about.html", timestamp=current_time, signedinas=SIGNEDIN_USER)

@app.route("/photo_gallery")
def photo_gallery():
    '''
    Photo Gallery Tab
    '''
    current_time = "Time Stamp: " + str(datetime.now())
    return render_template("photo_gallery.html",
                           timestamp=current_time, signedinas=SIGNEDIN_USER)

@app.route("/register")
def register():
    '''
        Register Tab
        '''
    current_time = "Time Stamp: " + str(datetime.now())
    return render_template("register.html", timestamp=current_time, failed_Attempt=True)

@app.route("/login")
def login():
    '''
    Login Tab
    '''
    current_time = "Time Stamp: " + str(datetime.now())
    return render_template("login.html", timestamp=current_time, error="")

@app.route("/handle_data", methods=['POST', 'GET'])
def handle_data():
    '''
    Method that handles data
    '''
    global SIGNEDIN_USER
    current_time = "Time Stamp: " + str(datetime.now())
    # see what service is needed (register, login, logout)
    service = request.args["service"]
    # Perform action based on requested service
    if service == "register":
        if not request.form['psw'] == request.form['psw-repeat']:
            return render_template("register.html",
                                   timestamp=current_time, error="Passwords Must Match!")
        if invalid_password(request.form['psw']):
            return render_template("register.html",
                                   timestamp=current_time, error="Invalid Password! "
            "Must contain 12 characters, at least 1 lowercase,"
            " 1 capital, 1 letter, and 1 special character")
        if save_data(request.form['username'], request.form['psw']):
            return render_template("register_success.html", timestamp=current_time)
        return render_template("register.html",
                               timestamp=current_time, error="Username Already Exists!")
    elif service == "login":
        username = request.form['username']
        if query_user(username, request.form['psw']):
            return render_template("index.html",
            timestamp=current_time, signedinas=SIGNEDIN_USER)
        return render_template("login.html",
        timestamp=current_time, error="Username/Password Incorrect!")
    elif service == "logout":
        SIGNEDIN_USER = ""
        return render_template("index.html", timestamp=current_time, signedinas=SIGNEDIN_USER)
    else:
        return "420 Request not Found"



# Start development web server
if __name__ == '__main__':
    app.run()
