from random import choice


rescued_cats = [{'pet_name': 'Alaska', 'user_id': 1, 'animal_type': 'cat', 'pet_type': 'rescued', 'gender': 'Female', 'breed': 'Domestic Short Hair', 'color': 'Tortoiseshell'}, {'pet_name': 'Athens', 'user_id': 2, 'animal_type': 'cat', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'Domestic Short Hair', 'color': 'White, Brown Tabby'}, {'pet_name': 'Bandit', 'user_id': 3, 'animal_type': 'cat', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'Domestic Short Hair', 'color': 'Black, White'}, {'pet_name': 'Bear', 'user_id': 4, 'animal_type': 'cat', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'Scottish Fold - Domestic Medium Hair', 'color': 'Brown Tabby'}, {'pet_name': 'Bella', 'user_id': 5, 'animal_type': 'cat', 'pet_type': 'rescued', 'gender': 'Female', 'breed': 'Domestic Short Hair', 'color': 'White, Black'}, {'pet_name': 'Bijou', 'user_id': 6, 'animal_type': 'cat', 'pet_type': 'rescued', 'gender': 'Female', 'breed': 'Domestic Short Hair', 'color': 'Blue, White'}, {'pet_name': 'Dakota', 'user_id': 7, 'animal_type': 'cat', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'Domestic Short Hair', 'color': 'Black'}, {'pet_name': 'Denver', 'user_id': 8, 'animal_type': 'cat', 'pet_type': 'rescued', 'gender': 'Female', 'breed': 'Domestic Short Hair', 'color': ''}, {'pet_name': 'Duchess', 'user_id': 9, 'animal_type': 'cat', 'pet_type': 'rescued', 'gender': 'Female', 'breed': 'Domestic Short Hair', 'color': 'Brown Tabby, White'}, {'pet_name': 'Echo', 'user_id': 10, 'animal_type': 'cat', 'pet_type': 'rescued', 'gender': 'Female', 'breed': 'Domestic Short Hair', 'color': 'White, Brown Tabby'}, {'pet_name': 'Everglades', 'user_id': 11, 'animal_type': 'cat', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'Domestic Short Hair', 'color': 'Brown Tabby'}, {'pet_name': 'Frank Sinatra Meatball', 'user_id': 12, 'animal_type': 'cat', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'Domestic Short Hair', 'color': 'White, Black'}, {'pet_name': 'Grand Canyon', 'user_id': 13, 'animal_type': 'cat', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'Domestic Short Hair', 'color': 'Brown Tabby'}, {'pet_name': 'Jayfeather', 'user_id': 14, 'animal_type': 'cat', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'Domestic Short Hair', 'color': 'Blue tabby, White'}, {'pet_name': 'Lopez', 'user_id': 15, 'animal_type': 'cat', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'Domestic Short Hair', 'color': 'Brown Tabby'}, {'pet_name': 'Marcus', 'user_id': 16, 'animal_type': 'cat', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'Domestic Short Hair', 'color': 'Brown Tabby'}, {'pet_name': 'Meow', 'user_id': 17, 'animal_type': 'cat', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'Domestic Short Hair', 'color': 'Brown Tabby'}, {'pet_name': 'Mikey', 'user_id': 18, 'animal_type': 'cat', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'Domestic Medium Hair', 'color': ''}, {'pet_name': 'Mo', 'user_id': 19, 'animal_type': 'cat', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'Domestic Short Hair', 'color': 'Brown Tabby'}, {'pet_name': 'Moonbeam', 'user_id': 20, 'animal_type': 'cat', 'pet_type': 'rescued', 'gender': 'Female', 'breed': 'Domestic Long Hair', 'color': 'Blue'}, {'pet_name': 'Mr. Peanut', 'user_id': 21, 'animal_type': 'cat', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'Domestic Short Hair', 'color': 'White, Black'}, {'pet_name': 'Niles', 'user_id': 22, 'animal_type': 'cat', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'Domestic Short Hair', 'color': 'White'}, {'pet_name': 'Ollie', 'user_id': 23, 'animal_type': 'cat', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'Domestic Short Hair', 'color': 'Brown Tabby, White'}, {'pet_name': 'Pascha', 'user_id': 24, 'animal_type': 'cat', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'Domestic Medium Hair', 'color': 'Blue'}, {'pet_name': 'Princess', 'user_id': 25, 'animal_type': 'cat', 'pet_type': 'rescued', 'gender': 'Female', 'breed': 'Domestic Short Hair', 'color': 'Brown Tabby, White'}, {'pet_name': 'Raspberry', 'user_id': 26, 'animal_type': 'cat', 'pet_type': 'rescued', 'gender': 'Female', 'breed': 'Domestic Short Hair', 'color': 'White, Dilute tortoiseshell'}, {'pet_name': 'Raven', 'user_id': 27, 'animal_type': 'cat', 'pet_type': 'rescued', 'gender': 'Female', 'breed': 'Domestic Short Hair', 'color': 'White, Black'}, {'pet_name': 'Redwood', 'user_id': 28, 'animal_type': 'cat', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'Domestic Short Hair', 'color': 'Brown Tabby'}, {'pet_name': 'Rosalina', 'user_id': 29, 'animal_type': 'cat', 'pet_type': 'rescued', 'gender': 'Female', 'breed': 'Domestic Short Hair', 'color': 'Black, White'}, {'pet_name': 'Samson', 'user_id': 30, 'animal_type': 'cat', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'Siamese', 'color': 'White, Seal Point'}, {'pet_name': 'Scarface', 'user_id': 31, 'animal_type': 'cat', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'Domestic Short Hair', 'color': 'White, Black'}, {'pet_name': 'Socks', 'user_id': 32, 'animal_type': 'cat', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'Domestic Short Hair', 'color': 'White, Brown Tabby'}, {'pet_name': 'Stormy', 'user_id': 33, 'animal_type': 'cat', 'pet_type': 'rescued', 'gender': 'Female', 'breed': 'Domestic Short Hair', 'color': 'Blue'}]
rescued_dogs = [{'pet_name': 'Archibald', 'user_id': 1, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'American Pit Bull - Shepherd', 'color': 'Sable'}, {'pet_name': 'Atari', 'user_id': 2, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Female', 'breed': 'American Pit Bull', 'color': 'White, Brown'}, {'pet_name': 'Atlas', 'user_id': 3, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'German Shepherd', 'color': 'Black'}, {'pet_name': 'Bennett', 'user_id': 4, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'Labrador - American Staffordshire Terrier', 'color': 'White, Tan'}, {'pet_name': 'Bixby', 'user_id': 5, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'German Shepherd', 'color': 'Chocolate, Tan'}, {'pet_name': 'Buddy', 'user_id': 6, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'Rat Terrier - Mix', 'color': 'Tri Color'}, {'pet_name': 'Bunji', 'user_id': 7, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'Australian Cattledog - Australian Shepherd', 'color': 'Tri Color, Merle'}, {'pet_name': 'Cash', 'user_id': 8, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'Redbone Coonhound - Catahoula Leopard Dog', 'color': 'Red Merle'}, {'pet_name': 'Daisy', 'user_id': 9, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Female', 'breed': 'Chihuahua', 'color': 'White, Dapple'}, {'pet_name': 'Fjord', 'user_id': 10, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'Chihuahua - Mix', 'color': 'Tri Color'}, {'pet_name': 'Harley', 'user_id': 11, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Female', 'breed': 'American Pit Bull', 'color': 'White, Seal'}, {'pet_name': 'Hyde', 'user_id': 12, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'Siberian Husky', 'color': 'White, Sable'}, {'pet_name': 'Ivy', 'user_id': 13, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Female', 'breed': 'Chihuahua - Boston Terrier', 'color': 'Tri Color'}, {'pet_name': 'Lilly', 'user_id': 14, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Female', 'breed': 'Labrador - Australian Shepherd', 'color': 'White, Brown'}, {'pet_name': 'Lola', 'user_id': 15, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Female', 'breed': 'Chihuahua - Border Terrier', 'color': 'Tri Color'}, {'pet_name': 'Luca', 'user_id': 16, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'American Staffordshire Terrier - Mix', 'color': 'White, Brown'}, {'pet_name': 'Maverick', 'user_id': 17, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'Shepherd - Terrier', 'color': 'Red'}, {'pet_name': 'Maxamillion', 'user_id': 18, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'American Pit Bull', 'color': 'White, Brindle'}, {'pet_name': 'Miss Ivy', 'user_id': 19, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Female', 'breed': 'American Pit Bull - Mix', 'color': 'White, Brindle'}, {'pet_name': 'Penny', 'user_id': 20, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Female', 'breed': 'Border Collie - Australian Shepherd', 'color': 'Tri Color'}, {'pet_name': 'Pip', 'user_id': 21, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Female', 'breed': 'German Shepherd', 'color': 'Black'}, {'pet_name': 'Pj', 'user_id': 22, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Female', 'breed': 'Neapolitan Mastiff', 'color': 'Brindle'}, {'pet_name': 'Reuben', 'user_id': 23, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'Blue Heeler', 'color': 'Spotted, Red Merle'}, {'pet_name': 'Rex', 'user_id': 24, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'Great Pyrenees', 'color': 'White'}, {'pet_name': 'Riley', 'user_id': 25, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Female', 'breed': 'Shepherd', 'color': 'Brown'}, {'pet_name': 'Ritz', 'user_id': 26, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Female', 'breed': 'German Shepherd', 'color': 'White, Black'}, {'pet_name': 'Roo', 'user_id': 27, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'Labrador - Mix', 'color': 'White, Black'}, {'pet_name': 'Sadie', 'user_id': 28, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Female', 'breed': 'Beagle - American Pit Bull', 'color': 'White, Brown'}, {'pet_name': 'Squirm', 'user_id': 29, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'Chihuahua', 'color': 'White, Tan'}, {'pet_name': 'Tex', 'user_id': 30, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'American Pit Bull - Mix', 'color': 'White, Brindle'}]


dates = ['05-01-22', '04-29-22', '04-15-22', '04-05-22']

locations = [ "1540 W El Camino Ave, Sacramento, CA 95833", "5309 Sunrise Blvd, Fair Oaks, CA 95628", "1117 Roseville Square, Roseville, CA 95678", "850 E Bidwell St, Folsom, CA 95630", ]

def add_location(list_pets, locations):
    new_list_pets = []
    for pet in list_pets:
        pet["location"]=str(choice(locations))
        new_list_pets.append(pet)
        pet['lat'] = 38.6681981
        pet['lng'] = -121.2382059
        pet['date']=choice(dates)
    return new_list_pets

list_rescued_dogs = add_location(rescued_dogs, locations)
print(list_rescued_dogs)

list_rescued_cats = add_location(rescued_cats, locations)
#print(list_rescued_cats)

