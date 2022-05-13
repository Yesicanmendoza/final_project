"""Models for movie ratings app."""

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
    """Data model for the users"""

    __tablename__ = "users" #create user incomplete information

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    fname = db.Column(db.String, nullable=False)
    lname = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    

    
    def __repr__(self):
        return f'<User fname={self.fname} lname={self.lname} email={self.email}>'



class Pet(db.Model):
    """Data model for a pet"""

    __tablename__ = "pets"

    pet_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    name = db.Column(db.String, nullable=True)
    animal_type = db.Column(db.String, nullable=False)
    pet_type = db.Column(db.String, nullable=False)
    gender = db.Column(db.String, nullable=False)
    breed = db.Column(db.String, nullable=False)
    color = db.Column(db.String, nullable=False)
    zip_code = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    
    user = db.relationship("User", backref="pets")

    def __repr__(self):
        return f'<Pet animal_type={self.animal_type} pet_type={self.pet_type}>'



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
