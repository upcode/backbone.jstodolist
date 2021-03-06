from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

db = SQLAlchemy(app)

##############################################################################
                ##### MODEL FOR USER TABLE ####
##############################################################################

class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(50), nullable=True)
    username = db.Column(db.String(20), nullable=True)
    password = db.Column(db.String(128))
   
    
##############################################################################
                        ##### HELPER FUNCTIONS ####
##############################################################################


def connect_to_db(app):
    """Connect the database to our Flask App"""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    # Prepare SQLAlchemy for connection
    db.app = app
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # Makes the connection
    db.init_app(app)

##############################################################################

if __name__ == "__main__":
# As a convenience, if we run this module interactively, it will leave
# you in a state of being able to work with the database directly.

    from routes import app
    connect_to_db(app)
    print "#### ** Conected to the Database ** ##"