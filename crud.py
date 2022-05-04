"""CRUD operations."""

from model import db, User, Pet, connect_to_db

def create_user(email, password):
    """Create and return a new user."""

    user = User(fname=fname, lname=laname,
                email=email, password=password,
                created_at=created_at)

    return user


def get_users():
    """Return all users."""

    return User.query.all()


def get_user_by_id(user_id):
    """Return user details."""

    return User.query.get(user_id)


def get_user_by_email(email):
    """Return the user if exits"""

    return User.query.filter(User.email == email).first()

#get user with lost pets
#get user with rescued pets

#Create pet
#Get rescued pets
#Get lost pets

if __name__ == '__main__':
    from server import app
    connect_to_db(app)