from bs4 import BeautifulSoup
import requests

url = "https://www.oregonhumane.org/adopt/?type=dogs"

#"https://www.oregonhumane.org/adopt/?type=cats"
#"https://www.oregonhumane.org/adopt/?type=dogs"

result = requests.get(url).text

doc = BeautifulSoup(result, "html.parser")

info_pets = doc.find_all("div", class_="result-item")

#print(info_pets)


pets= []
user_id = 1
#1
for info_pet in info_pets:
   
   pet = {}
   name  = info_pet.find("span", class_="name").text.strip()
   pet["pet_name"] = name

   pet["user_id"] = user_id

   pet["animal_type"]= "dog"
   #"cat"
   #dog

   pet["pet_type"] = "rescued"

   gender = info_pet.find("span", class_="sex").text.strip()
   pet["gender"] = gender

   breed = info_pet.find("span", class_="breed").text.strip()
   pet["breed"] = breed

   color = info_pet.find("span", class_="color").text.strip()
   pet["color"] = color

   img = info_pet.find("img").get('src')
   pet["img"] = img


   user_id = user_id + 1



   pets.append(pet)


print(pets)

 
   

    
    






    