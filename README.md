# The Pet Tracker
It's an app to help user find a lost pet. This application works by setting up a database of lost and rescued pets; and a written algorithm based on to pet characteristics and distance to match rescued pets with the most likely matched lost. The search criteria are based on the following information: Animal type, gender, the dates of the loss or rescue of the pet, breed, color, and that there is no more than 30 miles between the zone where the animal was lost and rescued. The user can create an account with an encrypted password, log on and log off. The app takes account of the various possibilities in which a user can input the information (whether to use uppercase letters, whether to use commas "," and forget to enter data).


## Technologies Required

- Python
-  Javascript
-  React
-  Flask
-  HTML
-  CSS
-  Jinja
-  AJAX
-  Bootstrap
-  SQLAlchemy

## APIs used

- Google Maps API
- Cloudinary API
 

## How to use this app

### Homepage

The homepage has a description about how the apps work and some tips about what to do in case that you have lost o rescued a pet.
In this part, you must create an account and log in to be able to use the navigation menu.

![Homepage](https://user-images.githubusercontent.com/80706744/178648646-32f5139d-b299-4e0d-986f-7348ea50f371.PNG)



### Pet Registration

You must select the option of Register a lost/rescued pet from the navigation menu and enter the pet's information.
The database has been fed with 30 rescued dogs and 30 rescued cats.
If you want to look for a match of those pets, you should consider that those pets were rescued at April-01-2022, so if you enter that your pet got lost after that date, there won't be matched. Another thing to know is that those pets are in the Sacramento area and the algorithm requires there is no more than 30 miles between the zone where the animal was lost and rescued.

![Pet registration](https://user-images.githubusercontent.com/80706744/178648775-231ae0ed-0ef3-4fd5-b18c-49893c1b67ae.PNG)

Other way to test this app is you can register lost and rescued pets, and check if they match.

### Look for a pet
You will be redirected to this part of the app as soon as you finish the pet registration, but also you can access through the navigation menu.
This section of the app will show you the pet you have registered and give you the next options:
- Look for your pet.
- Stoop looking for your pet.

And you just need to click on the pet's name to do the option you have chosen.

![Looking a match](https://user-images.githubusercontent.com/80706744/178648847-15fd1528-2e70-467c-b675-b4eb0c769746.PNG)



### Showing the matches

After clicking on your pet's name you will be redirected to the last part of the app, where you can see if there are matched pets or not. In the first case, you will be able to see the picture of the pet and the email of the user that registered it, so you can contact this person.
In case that you have found the pet you were looking for, you must submit the id of the pet, so  we can remove your pet and the matched one from the database.

![Matchedfound](https://user-images.githubusercontent.com/80706744/178649524-31df24cb-97a6-4833-b582-e649d793586e.PNG)
