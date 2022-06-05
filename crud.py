"""CRUD operations."""

from model import db, User, Pet, connect_to_db
#from datetime import datetime



def create_user(fname, lname, email, password, created_at):#
    """Create and return a new user."""

    user = User(fname=fname, lname=lname,
                email=email, password=password,
                created_at=created_at)

    return user


def get_users():
    """Return all users."""

    return User.query.all()


def get_user_by_id(user_id): #
    """Return user details."""

    return User.query.get(user_id)


def get_user_by_email(email): #
    """Return the user if exits"""

    return User.query.filter(User.email == email).first()


def get_lost_pets_by_user_id(user_id): #
    """Return one lost pet o a list if exits"""
    
    return Pet.query.filter(Pet.user_id==user_id, Pet.pet_type=='lost').all()


def get_all_pets_by_user_id(user_id): #
    """Return all pets  if exist"""
    
    return Pet.query.filter(Pet.user_id==user_id).all()


def create_pet(user_id, name, animal_type, pet_type, 
            gender, breed, color, location, lat, lng, date, img): #
    """Create and return a new pet."""

    pet = Pet(user_id=user_id, name=name,
                animal_type=animal_type, pet_type=pet_type,
                gender=gender, breed=breed,
                color=color, location=location,
                lat=lat, lng=lng, date=date, img=img)

    return pet


def get_pets():
    """Return all pets."""

    return Pet.query.all()


def get_pet_by_id(pet_id):#
    """Return pet details."""

    return Pet.query.get(pet_id)

def get_rescued_pets(animal_type):#
    """Return a list of rescued pets by animal type"""
    return Pet.query.filter(Pet.animal_type == animal_type, Pet.pet_type=='rescued').all()


def get_lost_dogs():
    """Return a list of lost dogs"""
    return Pet.query.filter(Pet.animal_type =='dog', Pet.pet_type=='lost').all()


def get_lost_cats():
    """Return a list of rescued cats"""
    return Pet.query.filter(Pet.animal_type =='cat', Pet.pet_type=='lost').all()



if __name__ == '__main__':
    from server import app
    connect_to_db(app)