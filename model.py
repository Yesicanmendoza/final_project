"""Models for find your pet app."""

from flask_sqlalchemy import SQLAlchemy
#import crud

db = SQLAlchemy()


class User(db.Model):
    """Data model for the users"""

    __tablename__ = "users" #create user incomplete information

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    fname = db.Column(db.String)
    lname = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    created_at = db.Column(db.DateTime)
    

    
    def __repr__(self):
        return f'<User fname={self.fname} lname={self.lname} email={self.email}>'



class Pet(db.Model):
    """Data model for a pet"""

    __tablename__ = "pets"

    pet_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    name = db.Column(db.String)
    animal_type = db.Column(db.String)
    pet_type = db.Column(db.String)
    gender = db.Column(db.String)
    breed = db.Column(db.String)
    color = db.Column(db.String)
    location = db.Column(db.String)
    lat = db.Column(db.Integer)
    lng = db.Column(db.Integer)
    date = db.Column(db.DateTime)
    
    user = db.relationship("User", backref="pets")

    def __repr__(self):
        return f'<Pet name={self.name} animal_type={self.animal_type} pet_type={self.pet_type}>'



def connect_to_db(flask_app, db_uri="postgresql:///pets", echo=True):

    """Connect to database."""
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
