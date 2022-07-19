"""Server"""

from flask import (Flask, render_template, request, flash, session,
                   redirect, jsonify, url_for)
from model import connect_to_db, db
import crud

from jinja2 import StrictUndefined

from datetime import date
from datetime import datetime
from copy import copy
from werkzeug.security import check_password_hash as checkph
from werkzeug.security import generate_password_hash as genph

import cloudinary.uploader
import cloudinary.api
import os

CLOUDINARY_KEY = os.environ['CLOUDINARY_KEY']
CLOUDINARY_SECRET = os.environ['CLOUDINARY_SECRET']
CLOUD_NAME = 'yesicamendoza'


app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined



@app.route('/')
def homepage():
    """View homepage."""
    user_id = session.get("user_id")
    #print(user_id)
    return render_template('homepage.html', user_id=user_id)


@app.route("/users", methods=["POST"])
def register_user():
    """Create a new user."""
    #Get user info
    fname = (request.form['fname']).title()
    lname = (request.form['lname']).title()
    email = (request.form['email']).lower()
    password = genph(request.form["password"])
    created_at = date.today()

    #Validation of user info
    user_info = [fname, lname, email, password, created_at]
    
    for data in user_info:
        if data == '':
            info_completed = False
            break
        else:
            info_completed = True

    

    #Verification that email is not in db and create a new User
    if info_completed == False:
        flash("Please enter all the information.")
    
    else:
            if crud.get_user_by_email(email):
                flash("An user with that email already exists. Please enter a different email.")

            else:
                user = crud.create_user(fname, lname, email, password, created_at)
                db.session.add(user)
                db.session.commit()
                flash("Your account has successfully been created. You may now log in.")
  
            

    return redirect("/")



@app.route("/login", methods=['POST'])
def user_login():
    """Check the password and log in."""

    email = (request.form['email']).lower()
    password = request.form["password"]

    user = crud.get_user_by_email(email)
    #If the user has logged in, get the user's ans pet´s information
    if user:
        if checkph(user.password, password):
            session['user_id']= user.user_id
            session['user_fname']= user.fname
                   
            flash('Logged in, now you can use the Navigation menu!')

        else:
            flash('Wrong password.')

    else:
        flash("Please create an account.")

    return redirect('/')


@app.route("/logout", methods=['GET'])
def log_out():
    """User can log out."""
    session['user_id']= None
    session['user_fname']= None
    flash("You have logged out.")

    return redirect('/')


@app.route("/register_a_pet")
def pet_register_form():
    """Show register pet form."""    
    return render_template('Pet_registration.html')


@app.route("/show_reg_form")
def show_reg_form():
    """show the form if the user has logged in."""
    user_id = session.get("user_id")
    
    msg = ''
    if user_id is None:
        msg ='Please log in.'

    return jsonify({'msg': msg})



@app.route("/pet_registration.json", methods=["POST"])
def register_pet():
    """Create a new pet."""
    user_id = session.get("user_id")
    msg = ""    
   
    if user_id:
        
        name = request.json.get('name').title() 
        animal_type=request.json.get('animal_type')
        pet_type=request.json.get('pet_type')
        gender=request.json.get('gender').lower()
        breed=request.json.get('breed').lower()        
        color=request.json.get('color').lower()
        location=request.json.get('location')
        center=request.json.get('center')
        string_date=request.json.get('date')
        lat=request.json.get('lat')
        lng=request.json.get('lng')
        
        #Validation of pet info
        info_completed = False

        if name =='':
            name="Unknown"

        #Address validation
        
        if lat == '':
           address_val = None
        else:
            address_val = True

        
            #Date validation
        try:
            date=datetime.strptime(string_date, "%Y-%m-%d")

        except ValueError:
            date_val = None
        
        else:
            if date > date.today():
                date_val = None 
            else:
                date_val = True
                #If address and date are ok, check the rest of the info
                 
        pet_info = [breed, color, location]
        count = 0              
        for data in pet_info:
            if data == '' or data == None:             
                break
            else:                
                count = count + 1                            

        if count == 3 and address_val == True and  date_val == True:                        
            info_completed = True   
            


        if info_completed == True:               
            img="/static/img/Noimage.PNG"
            if animal_type == 'cat':
                img="/static/img/CAT.png"
            #Create a new pet 
            pet = crud.create_pet(user_id, name, animal_type, pet_type, 
                gender, breed, color, location, lat, lng, date, img)
            db.session.add(pet)
            db.session.commit()
            msg = "The information was saved, please continue with the step two."
            session['new_pet_id']=pet.pet_id
            new_pet_id = session.get('new_pet_id')

        else:
            if address_val == None:
                msg = "Please enter a valid address. Hint: Copy the address displayed by Google Maps"
            elif date_val == None:
                msg = "Please enter a valid date."
            elif count <3:
                msg ="Please enter all the information."

    return jsonify({'msg': msg})


@app.route("/register_a_pet/pet_image", methods=['POST'])
def get_url_img():
    """Get the image of the pet."""
    new_pet_id = session.get('new_pet_id')

    if new_pet_id == None:
        flash("Please enter pet's information first")
        return redirect("/register_a_pet")

    else:   
           
        my_file = request.files["img"]
        if not my_file:
            flash("Please upload an image. DON'T DO THE REGISTRATION AGAIN")
            return redirect("/register_a_pet")

        result =  cloudinary.uploader.upload(my_file, 
                                                api_key=CLOUDINARY_KEY, 
                                                api_secret=CLOUDINARY_SECRET, 
                                                cloud_name=CLOUD_NAME)
                
        img=result['secure_url']   
        pet=crud.get_pet_by_id(new_pet_id)
        pet.img = img
        db.session.commit()
        flash("Your pet has successfully been registered.")
        session['new_pet_id']=None
        
    return redirect("/look_for_pet")



@app.route('/look_for_pet/')
def get_pet_information():
    "Get infotmation about the pet(s) to look for"
    #Get user info    
    user_id = session.get("user_id")
    #Set variables
    session['new_pet_id']=None 
    fname = 'Uknown'
    pets_to_look=[]

    if user_id is None:
        msg='Please log in.'
          
    #Get user's pets
    else:
        fname = session["user_fname"]
        all_pets = []
        all_pets = crud.get_all_pets_by_user_id(user_id)

        for pet in all_pets:
            if pet.pet_type != 'found': 
                pets_to_look.append(pet)


        if len(pets_to_look)== 0:
            msg = f"{fname}, you do not have pets to look for."
        else:            
            if len(pets_to_look)==1:
                msg = f"{fname}, click on your pet's name to look for a match."
            else:
                msg = f"{fname}, select one pet to look for by clicking the name."

            

    return render_template('Showing_lost_pet.html', msg=msg, 
                            fname=fname, pets=pets_to_look)



@app.route('/lost_pet/<pet_id>/found')
def update_pet_type(pet_id):
    """Change the status of the selected pet"""
    #If user does not want to continue loking for a pet
    #change the pet type to found
    pet = crud.get_pet_by_id(pet_id)
    pet.pet_type = 'found'
    db.session.commit()
    flash('We have changed the status of your pet to "found".')

    user_id = session.get("user_id")
    all_pets = crud.get_all_pets_by_user_id(user_id)

    if len(all_pets) >=1:
        return redirect("/look_for_pet")

    return redirect('/')




@app.route('/lost_pet/<pet_id>/')
def show_list_matches(pet_id):
    """Show template matches and get id of pet to look for"""
    session['pet_id'] = pet_id
    
    return render_template('matches.html')



@app.route('/matches.json')
def get_matches():
    """Get the matches of the chosen pet (pet to look for)"""
    #Get pet chosen info
    pet_id = session['pet_id']
    pet_to_look = crud.Pet.query.get(pet_id)
    animal_type = pet_to_look.animal_type
    pet_type = pet_to_look.pet_type

    #Look according of the pet type
    if pet_type=="lost":
        pet_list=crud.get_rescued_pets(animal_type)
    elif pet_type=="rescued":
        pet_list=crud.get_lost_pets(animal_type)   
        
    matches = []
    #Define matches according to the search criteria
    for pet in pet_list:
        if pet.gender == pet_to_look.gender and pet.date >= pet_to_look.date:
            
            pet_breed_lst=[]
            pet_breed = copy(pet.breed)
            #Code to check if, least, one in breed matches
            if ',' in pet.breed:
                pet_breed=pet.breed.split(',')
            elif ' ' in pet.breed:
                pet_breed=pet.breed.split(' ')             
            if type(pet_breed) == type(pet_breed_lst):
                pet_breed_lst.extend(pet_breed)
            else:
                pet_breed_lst.append(pet_breed)            
            
            
            pet_look_breed_lst=[]
            pet_to_look_breed = copy(pet_to_look.breed)
            if ',' in pet_to_look.breed:
                pet_to_look_breed=pet_to_look.breed.split(',')
            elif ' ' in pet_to_look.breed:
                pet_to_look_breed=pet_to_look.breed.split(' ')
            if type(pet_to_look_breed)==type(pet_look_breed_lst):        
                pet_look_breed_lst.extend(pet_to_look_breed)
            else:
                pet_look_breed_lst.append(pet_to_look_breed)
            
            breed = False
            if len(pet_breed_lst) > 1:
                for word in pet_breed_lst:
                    if word in pet_look_breed_lst:
                        breed = True                        
                        break
            else:
                if pet_breed_lst[0] in pet_look_breed_lst:
                    breed = True

            #Code to check if, least, one word in color matches
            pet_color_lst=[]
            pet_color = copy(pet.color)
            if ',' in pet.color:
                pet_color=pet.color.split(',')
            elif ' ' in pet.color:
                pet_color=pet.color.split(' ')            
            

            if type(pet_color)==type(pet_color_lst):        
                pet_color_lst.extend(pet_color) 
            else:
                pet_color_lst.append(pet_color)           
            
            
            pet_look_color_lst=[]
            pet_to_look_color=copy(pet_to_look.color)
            if ',' in pet_to_look.color:
                pet_to_look_color=pet_to_look.color.split(',')
            elif ' ' in pet_to_look.color:
                pet_to_look_color=pet_to_look.color.split(' ') 
                        
            
            if type(pet_to_look_color)== type(pet_look_color_lst):
                pet_look_color_lst.extend(pet_to_look_color)
            else:
                pet_look_color_lst.append(pet_to_look_color)           
            
            color = False
            if len(pet_color_lst) >1:
                for word in pet_color_lst:
                    if word in pet_look_color_lst:
                        color = True
                        print(word)
                        print(color)
                        break
            else:
                if pet_color_lst[0] in pet_look_color_lst:
                    color = True
            
            if breed==True and color==True:
                matches.append(pet)            
    

    matches_and_pet_to_look = []

    if len(matches)==0:               
        msg = 'There are not matched.'
        matches_and_pet_to_look = None
        
    else:
        msg = 'Showing the matches:'
        matches.append(pet_to_look)
       
        
        #Changing the pets object, for a dictionary
        #The distance will be check by the jsx file
        for pet in matches:
            pet_dict = {}
            pet_dict['pet_id'] = pet.pet_id
            pet_dict['name'] = pet.name
            #pet_dict['animal_type'] = pet.animal_type
            pet_dict['pet_type'] = pet.pet_type
            pet_dict['gender'] = pet.gender  
            pet_dict['breed'] = pet.breed
            pet_dict['color'] = pet.color  
            pet_dict['date'] = pet.date 
            pet_dict['location'] = pet.location
            pet_dict['lat'] = pet.lat
            pet_dict['lng'] = pet.lng
            pet_dict['img'] = pet.img
            pet_dict['date'] = f'{pet.date.date()}'
            pet_dict['user_type'] = "Rescuer"
            if pet.pet_type == 'lost':
               pet_dict['user_type'] = "Owner"               
            pet_user = crud.get_user_by_id(pet.user_id)
            pet_dict['user_name'] = pet_user.fname
            pet_dict['user_email'] = pet_user.email
            
            matches_and_pet_to_look.append(pet_dict)

    
    return jsonify({'msg': msg, 'matches_and_pet_to_look':matches_and_pet_to_look})


@app.route("/change_pet_type.json", methods=["POST"])
def change_pet_type():
    """Change the pet type to found."""  
    msg2=''
    id_lost_pet = session['pet_id'] 
    print(request.json.get('match_pet_id'))        
    id_match_pet = request.json.get('match_pet_id') 
    lost_pet=crud.get_pet_by_id(id_lost_pet)
    lost_pet.pet_type='found'
    match_pet=crud.get_pet_by_id(id_match_pet)
    match_pet.pet_type='found'    
    db.session.commit()
    msg2 = f'We have changed the status to "found" of the pets No. {id_lost_pet} and No. {id_match_pet}.'
    return jsonify({'msg2': msg2})
    

    
if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
