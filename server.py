"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect, jsonify)
from model import connect_to_db, db
import crud

from jinja2 import StrictUndefined

from datetime import date
from datetime import datetime


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
    fname = request.form['fname']
    lname = request.form['lname']
    email = request.form['email']
    password = request.form["password"]
    created_at = date.today()

    #Validation of user info
    user_info = [fname, lname, email, password, created_at]
    info_completed = None
    for data in user_info:
        if data == '':
            flash("Please fill up all information spaces.")
            break
        else:
            info_completed = True

    #Verification that email is not in db and create a new User
    if info_completed:
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

    email = request.form['email']
    password = request.form["password"]

    user = crud.get_user_by_email(email)

    if user:
        if user.password == password:
            session['user_id']= user.user_id
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
        flash('Please log in.')        
    
    else:
        
        name = request.json.get('name') #Can be None
        animal_type=request.json.get('animal_type')
        pet_type=request.json.get('pet_type')
        gender=request.json.get('gender')
        breed=request.json.get('breed')#Sugestions about how to know the breed
        color=request.json.get('color')
        zip_code=request.json.get('zip_code')#Check that is a real zc
        date=datetime.strptime((request.json.get('date')), "%m-%d-%y")
        
        pet = crud.create_pet(user_id, name, animal_type, pet_type, 
            gender, breed, color, zip_code, date)
        db.session.add(pet)
        db.session.commit()
        result_text = f"Your pet has successfully been registrated."

    return jsonify({'msg': result_text})



@app.route('/look_for_pet/')
def get_user_type():
    """View filter to look for a pet."""
    user_id = session.get("user_id")
    list_pets = crud.get_list_pets_by_user_id(user_id)
    user_type = "User with rescued pet(s)"
    for pet in list_pets:
        if pet.pet_type=="lost":
            user_type = "User with a lost pet"

    return render_template('Looking_lost_pet.html', user_type=user_type, user_id=user_id)

  


    

    
if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
