import os
import json
from random import choice, randint
from datetime import datetime
from werkzeug.security import generate_password_hash as genph

import data
import crud
import model
import server

os.system("dropdb pets")
os.system('createdb pets')

model.connect_to_db(server.app)
model.db.create_all()

#Create user
users_in_db=[]
for index, name in enumerate(data.first_names):
    fname = name.title()
    lname = (choice(data.last_names)).title()
    email = f'{name.lower()}{index}@email.com'
    password = genph('1234')
    created_at = datetime.strptime(f'05-08-22', "%m-%d-%y")

    user_in_db=crud.create_user(fname, lname, email,
                                 password, created_at)
    users_in_db.append(user_in_db)

model.db.session.add_all(users_in_db)
model.db.session.commit()

def create_db_rescued_pets(list_of_pets, animal_type):
    """Create a list of pet objets"""

    rescued_pet_in_db = []
    for pet in list_of_pets:
        user_id = pet["user_id"]
        name = (pet["pet_name"]).title()
        pet_type = "rescued"
        gender = (pet["gender"]).lower()
        breed = (pet["breed"]).lower()
        color = (pet["color"]).lower()
        location = pet["location"]   
        lat=pet['lat'] 
        lng=pet['lng']
        date = datetime.strptime(pet["date"], "%m-%d-%y")
        img=pet['img']
    
        db_rescued_pet= crud.create_pet(
            user_id, name, animal_type, pet_type, 
            gender, breed, color, location, lat, lng, date, img)

        rescued_pet_in_db.append(db_rescued_pet)

    
    return rescued_pet_in_db 

#Create a db for rescued dogs
rescued_dogs_in_db=create_db_rescued_pets(data.list_rescued_dogs, "dog")
model.db.session.add_all(rescued_dogs_in_db)
model.db.session.commit()


#Create a db for rescued cats
#rescued_cats_in_db=create_db_rescued_pets(data.list_rescued_cats, "cat")
#model.db.session.add_all(rescued_cats_in_db)
#model.db.session.commit()


