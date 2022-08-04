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

![Homepage](https://user-images.githubusercontent.com/80706744/182918991-71e85210-e275-4bc3-bf49-7cbee431fb9b.PNG)


### Pet Registration

You must select the option of Register a lost/rescued pet from the navigation menu and enter the pet's information.
The database has been fed with 30 rescued dogs and 30 rescued cats.
If you want to look for a match of those pets, you should consider that those pets were rescued at April-01-2022, so if you enter that your pet got lost after that date, there won't be matched. Another thing to know is that those pets are in the Sacramento area and the algorithm requires there is no more than 30 miles between the zone where the animal was lost and rescued.

![Pet registration](https://user-images.githubusercontent.com/80706744/182919162-457d99e7-5f94-48f7-8453-2af39a869fa6.PNG)


Other way to test this app is you can register lost and rescued pets, and check if they match.

### Look for a pet
You will be redirected to this part of the app as soon as you finish the pet registration, but also you can access through the navigation menu.
This section of the app will show you the pet you have registered and give you the next options:
- Look for your pet.
- Stoop looking for your pet.

And you just need to click on the pet's name to do the option you have chosen.

![Looking a match](https://user-images.githubusercontent.com/80706744/182919248-3fb125a1-8798-40c9-b7e3-167ba32d1323.PNG)




### Showing the matches

After clicking on your pet's name you will be redirected to the last part of the app, where you can see if there are matched pets or not. In the first case, you will be able to see the picture of the pet and the email of the user that registered it, so you can contact this person.
In case that you have found the pet you were looking for, you must submit the id of the pet, so  we can remove your pet and the matched one from the database.

![Matchedfound](https://user-images.githubusercontent.com/80706744/182919331-d18efff2-3b6c-40e7-9b98-978cd4e6fc06.PNG)
