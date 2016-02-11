##############################################################################
                ##### CONTROLLER, ROUTES, VIEW  ####
##############################################################################
import os
from flask import Flask
from flask import Flask, render_template, redirect, request, url_for, flash, session
from flask_wtf import Form
from flask import jsonify
from datetime import datetime
from flask import send_from_directory
from werkzeug import secure_filename
from flask_debugtoolbar import DebugToolbarExtension
# IMPORTED MODEL TABLES TO ROUTES
from model import User
from model import connect_to_db, db
##############################################################################

app = Flask(__name__)
app.secret_key = 'RED PANDA'
##############################################################################

app.secret_key = os.environ.get("FLASK_SECRET_KEY", "freedom")
##############################################################################
                        ## LOGIN ROUTE ##
##############################################################################

# @app.route('/', methods=['GET'])
# def login():
#     """Show login form."""

#     return render_template("login.html")


# @app.route('/login-process', methods=['POST'])
# def process_login():
#     """Log user into site, find user in the DB and their
#     their user id in the session then if they
#      are logged in redirect them to map page"""

#     # Get form variables
#     email = request.form["email"]
#     password = request.form["password"]

#     # printing data from form to BASH
#     print "form password"

#     print password

#     # check user exisit and then asign them variable user
#     user = User.query.filter_by(email=email).first()

#     print "\n \n \n ", user

#     # Conditions
#     if not user:

#         flash("No such user")

#         return redirect("/")

#     elif user.password != password:

#         flash("Incorrect password")

#         return redirect("/")
#     else:
#         session["user_id"] = user.user_id

#     flash("Logged in")

#     return redirect('/index')

# ##############################################################################
#                         ## LOG OUT ROUTE ##
# ##############################################################################

# @app.route("/logout")
# def process_logout():
#     """removing user_id from session to logout user"""

#     print " LOGGED OUT USER "

#     del session["user_id"]

#     flash("You have Successfully Logged Out!")

#     return redirect("/")

# ##############################################################################
#                             # # REGISTER ROUTE # #
# ##############################################################################


# @app.route('/register-process', methods=['POST'])
# def register_processed():
#     """New user signup form"""

#     print "REGISTER ROUTE IS WORKING"

#     # Get variables from HTML form
#     email = request.form["email"]

#     password = request.form["password"]

#     # query the DB for user
#     new_user = User(email=email, password=password)

#     # check DB for user searching by email
#     same_email_user = User.query.filter(User.email == email).first()

#     # users who registered / login will be redircted --> list-page
#     if same_email_user:
#         flash("Email is already registered. Please signin to your account")
#         return redirect("/")

#     # check user by username --> condition to authentiate user
#     same_username = User.query.filter(User.email == email).first()
#     if same_username:
#         flash("please pick another username")
#         return redirect("/")

#         # add user to db if they are new
#     db.session.add(new_user)
#         # commit transaction
#     db.session.commit()

#     # query db user by email add them to current session and redirect
#     # user to passport page

#     user = User.query.filter_by(email=email).first()

#     flash("User %s added.You have successfully created an account! Welcome to Live Simply" % email)

#     session["user_id"] = user.user_id

#     return redirect("/index")

##############################################################################
                        # #  List Page # #
##############################################################################

@app.route('/index')
def index():
    """List page"""

    # user_id = session['user_id']



    return render_template('index.html')


##############################################################################
@app.route('/contact')
def contact():
    """Contact Page"""

    # user_id = session['user_id']



    return render_template('contact.html')

@app.route('/about')
def about():
    """ About Page"""

    # user_id = session['user_id']



    return render_template('about.html')

##############################################################################

# @app.route('/index2')
# def plainJS():
#     """List page"""

#     user_id = session['user_id']



#     return render_template('index2.html')
##############################################################################
@app.route("/error")
def error():
    raise Exception("Error!")

##############################################################################
# HELPER FUNCTIONS
##############################################################################


if __name__ == "__main__":
    
    PORT = int(os.environ.get("PORT", 5000))
    DEBUG = "NO_DEBUG" not in os.environ

    app.run(debug=DEBUG, host="0.0.0.0", port=PORT)