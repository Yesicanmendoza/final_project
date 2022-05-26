"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect, jsonify)
from model import connect_to_db, db
import crud

from jinja2 import StrictUndefined

from datetime import date
from datetime import datetime
from werkzeug.security import check_password_hash as checkph
from werkzeug.security import generate_password_hash as genph


app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined



@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')


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
        flash("Please fill up all information spaces.")
    
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
                   
            flash('Logged in!')

        else:
            flash('Wrong password.')

    else:
        flash("Please create an account.")

    return redirect('/')


@app.route("/register_a_pet")
def pet_register_form():
    """Show register pet form."""

    return render_template('Pet_registration.html')



@app.route("/pet_registration.json", methods=["POST"])
def register_pet():
    """Create a new pet."""
    user_id = session.get("user_id")
    
    if user_id is None:
        msg ='Please log in.'
          

    else:
        
        name = request.json.get('name').title() #Can be None
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
        if lat == '':
            msg = "Please introduce a valid address"
        
        else:            
            pet_info = [animal_type, pet_type, 
                    gender, breed, color, location, 
                    lat, lng, string_date]
    
            for data in pet_info:
                if data == '' or data == None:
                    info_completed = False
                    break
                else:
                    info_completed = True

            if info_completed == False:
                msg =f"Please fill up all information spaces."
              
            else:
                date=datetime.strptime(string_date, "%m-%d-%y")
                pet = crud.create_pet(user_id, name, animal_type, pet_type, 
                    gender, breed, color, location, lat, lng, date)
                db.session.add(pet)
                db.session.commit()
                msg = "Your pet has successfully been registrated."

    return jsonify({'msg': msg})




@app.route('/look_for_pet/')
def get_pet_information():
    "Get infotmation about the pet(s) to look for"
    #Get user info    
    user_id = session.get("user_id") 
    fname = 'Uknown'
    lost_pets = []

    if user_id is None:
        msg='Please log in.'
          
    #Define user type
    else:
        fname = session["user_fname"]
    
        all_pets = crud.get_all_pets_by_user_id(user_id)
        if len(all_pets)== 0:
                session['user_type']= 'no_pet'
        else:
            
            lost_pets = crud.get_lost_pets_by_user_id(user_id)

            if len(lost_pets) == 0:
                session['user_type']='rescue_pet'
            else:
                session['user_type']='look_pet'
   
        user_type=session['user_type']
        
        if user_type == 'no_pet' or user_type == 'rescue_pet':
            msg = f"{fname}, you do not have pets to look for"
        #Get list of pets
        elif user_type == 'look_pet':
            
            if len(lost_pets)==1:
                msg = f"{fname}, click in your pet's name."
            else:
                msg = f"{fname}, select one pet to look for a match."

            

    return render_template('Showing_lost_pet.html', msg=msg, 
                            fname=fname, pets=lost_pets)


@app.route('/lost_pet/<pet_id>/')
def show_list_matches(pet_id):
    """Show list of matches."""
    session['pet_id'] = pet_id
    
    return render_template('matches.html')



@app.route('/matches.json')
def get_pet_info():
    pet_id = session['pet_id']
    lost_pet = crud.Pet.query.get(pet_id)
    animal_type = lost_pet.animal_type

    all_rescued_pets = crud.get_rescued_pets(animal_type)
    
    matches = []
    for pet in all_rescued_pets:
        if pet.gender == lost_pet.gender and pet.date >= lost_pet.date:
            if lost_pet.breed in pet.breed:
                if lost_pet.color in pet.color:
                    matches.append(pet)            
    

    if len(matches)==0:               
        msg = 'There are not matches'
    
    else:
        msg = 'Here are the matches:'
        matches.append(lost_pet)
        #This is necesary fetch the lost pet info and 
        #matches info
        match_and_lost_pet= []
        #Changing the pets ogject, for a dictionary
        for pet in matches:
            pet_dict = {}
            pet_dict['pet_id'] = pet.pet_id
            pet_dict['name'] = pet.name
            pet_dict['animal_type'] = pet.animal_type
            pet_dict['pet_type'] = pet.pet_type
            pet_dict['gender'] = pet.gender  
            pet_dict['breed'] = pet.breed
            pet_dict['color '] = pet.color  
            pet_dict['date'] = pet.date 
            pet_dict['location'] = pet.location
            pet_dict['lat'] = pet.lat
            pet_dict['lng'] = pet.lng
            pet_user = crud.get_user_by_id(pet.user_id)
            pet_dict['user_name'] = pet_user.fname
            pet_dict['user_email'] = pet_user.email
            
            match_and_lost_pet.append(pet_dict)

    
    return jsonify({'msg': msg, 'match_and_lost_pet':match_and_lost_pet})













    

    
if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
