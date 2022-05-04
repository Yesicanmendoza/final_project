from random import choice

rescued_cats = [{'pet_name': 'Athena', 'user_id': 20, 'animal_type': 'cat', 'pet_type': 'rescued', 'gender': 'Female', 'breed': 'Domestic Short Hair', 'color': 'White, Torbi'}, {'pet_name': 'Athens', 'user_id': 21, 'animal_type': 'cat', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'Domestic Short Hair', 'color': 'White, Brown Tabby'}, {'pet_name': 'Bear', 'user_id': 22, 'animal_type': 'cat', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'Domestic Medium Hair', 'color': 'Brown Tabby'}, {'pet_name': 'Bella', 'user_id': 23, 'animal_type': 'cat', 'pet_type': 'rescued', 'gender': 'Female', 'breed': 'Domestic Short Hair', 'color': 'White, Black'}, {'pet_name': 'Bruce', 'user_id': 24, 'animal_type': 'cat', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'Domestic Short Hair', 'color': 'Brown Tabby'}, {'pet_name': 'Burton', 'user_id': 25, 'animal_type': 'cat', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'Domestic Short Hair', 'color': 'Black'}, {'pet_name': 'Carter', 'user_id': 26, 'animal_type': 'cat', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'Domestic Short Hair', 'color': 'White, Black'}, {'pet_name': 'Charlie', 'user_id': 27, 'animal_type': 'cat', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'Birman', 'color': 'Seal Bicolor'}, {'pet_name': 'Echo', 'user_id': 28, 'animal_type': 'cat', 'pet_type': 'rescued', 'gender': 'Female', 'breed': 'Domestic Short Hair', 'color': 'White, Brown Tabby'}, {'pet_name': 'Frank Sinatra Meatball', 'user_id': 29, 'animal_type': 'cat', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'Domestic Short Hair', 'color': 'White, Black'}, {'pet_name': 'Fuzzy Tail', 'user_id': 30, 'animal_type': 'cat', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'Domestic Medium Hair', 'color': 'Blue tabby'}, {'pet_name': 'Jellybean', 'user_id': 31, 'animal_type': 'cat', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'Domestic Short Hair', 'color': 'Red tabby'}, {'pet_name': 'Josie', 'user_id': 32, 'animal_type': 'cat', 'pet_type': 'rescued', 'gender': 'Female', 'breed': 'Domestic Medium Hair', 'color': 'Brown Tabby, White'}, {'pet_name': 'Kylo', 'user_id': 33, 'animal_type': 'cat', 'pet_type': 'rescued', 'gender': 'Female', 'breed': 'Domestic Short Hair', 'color': 'Brown Tabby'}, {'pet_name': 'Lopez', 'user_id': 34, 'animal_type': 'cat', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'Domestic Short Hair', 'color': 'Brown Tabby'}, {'pet_name': 'Love Ball', 'user_id': 35, 'animal_type': 'cat', 'pet_type': 'rescued', 'gender': 'Female', 'breed': 'Domestic Medium Hair', 'color': 'Torbi'}, {'pet_name': 'Mia', 'user_id': 36, 'animal_type': 'cat', 'pet_type': 'rescued', 'gender': 'Female', 'breed': 'Domestic Short Hair', 'color': 'Blue tabby'}, {'pet_name': 'Mikey', 'user_id': 37, 'animal_type': 'cat', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'Domestic Medium Hair', 'color': ''}, {'pet_name': 'Mouth', 'user_id': 38, 'animal_type': 'cat', 'pet_type': 'rescued', 'gender': 'Female', 'breed': 'Domestic Medium Hair', 'color': 'Black, White'}, {'pet_name': 'Niles', 'user_id': 39, 'animal_type': 'cat', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'Domestic Short Hair', 'color': 'White'}, {'pet_name': 'Pip', 'user_id': 40, 'animal_type': 'cat', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'Domestic Short Hair', 'color': 'Brown Tabby, White'}, {'pet_name': 'Raspberry', 'user_id': 41, 'animal_type': 'cat', 'pet_type': 'rescued', 'gender': 'Female', 'breed': 'Domestic Short Hair', 'color': 'Dilute tortoiseshell, White'}, {'pet_name': 'Samson', 'user_id': 42, 'animal_type': 'cat', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'Siamese', 'color': 'White, Seal Point'}, {'pet_name': 'Spooky', 'user_id': 43, 'animal_type': 'cat', 'pet_type': 'rescued', 'gender': 'Female', 'breed': 'Domestic Medium Hair', 'color': 'Tortoiseshell, White'}, {'pet_name': 'Um', 'user_id': 44, 'animal_type': 'cat', 'pet_type': 'rescued', 'gender': 'Female', 'breed': 'Domestic Short Hair', 'color': 'Black'}, {'pet_name': 'Woodrow', 'user_id': 45, 'animal_type': 'cat', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'Domestic Short Hair', 'color': 'Red tabby'}, {'pet_name': 'Yam', 'user_id': 46, 'animal_type': 'cat', 'pet_type': 'rescued', 'gender': 'Female', 'breed': 'Domestic Medium Hair', 'color': 'White, Black'}, {'pet_name': 'Yuri', 'user_id': 47, 'animal_type': 'cat', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'Domestic Short Hair', 'color': 'Black, White'}]
rescued_dogs = [{'pet_name': 'Archibald', 'user_id': 1, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'American Pit Bull - Shepherd', 'color': 'Sable'}, {'pet_name': 'Atari', 'user_id': 2, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Female', 'breed': 'American Pit Bull', 'color': 'White, Brown'}, {'pet_name': 'Atlas', 'user_id': 3, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'German Shepherd', 'color': 'Black'}, {'pet_name': 'Bennett', 'user_id': 4, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'Labrador - American Staffordshire Terrier', 'color': 'White, Tan'}, {'pet_name': 'Bixby', 'user_id': 5, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'German Shepherd', 'color': 'Chocolate, Tan'}, {'pet_name': 'Buddy', 'user_id': 6, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'Rat Terrier - Mix', 'color': 'Tri Color'}, {'pet_name': 'Bunji', 'user_id': 7, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'Australian Cattledog - Australian Shepherd', 'color': 'Tri Color, Merle'}, {'pet_name': 'Cash', 'user_id': 8, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'Redbone Coonhound - Catahoula Leopard Dog', 'color': 'Red Merle'}, {'pet_name': 'Daisy', 'user_id': 9, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Female', 'breed': 'Chihuahua', 'color': 'White, Dapple'}, {'pet_name': 'Fjord', 'user_id': 10, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'Chihuahua - Mix', 'color': 'Tri Color'}, {'pet_name': 'Harley', 'user_id': 11, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Female', 'breed': 'American Pit Bull', 'color': 'White, Seal'}, {'pet_name': 'Hyde', 'user_id': 12, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'Siberian Husky', 'color': 'White, Sable'}, {'pet_name': 'Ivy', 'user_id': 13, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Female', 'breed': 'Chihuahua - Boston Terrier', 'color': 'Tri Color'}, {'pet_name': 'Lilly', 'user_id': 14, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Female', 'breed': 'Labrador - Australian Shepherd', 'color': 'White, Brown'}, {'pet_name': 'Lola', 'user_id': 15, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Female', 'breed': 'Chihuahua - Border Terrier', 'color': 'Tri Color'}, {'pet_name': 'Luca', 'user_id': 16, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'American Staffordshire Terrier - Mix', 'color': 'White, Brown'}, {'pet_name': 'Maverick', 'user_id': 17, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'Shepherd - Terrier', 'color': 'Red'}, {'pet_name': 'Maxamillion', 'user_id': 18, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'American Pit Bull', 'color': 'White, Brindle'}, {'pet_name': 'Miss Ivy', 'user_id': 19, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Female', 'breed': 'American Pit Bull - Mix', 'color': 'White, Brindle'}, {'pet_name': 'Penny', 'user_id': 20, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Female', 'breed': 'Border Collie - Australian Shepherd', 'color': 'Tri Color'}, {'pet_name': 'Pip', 'user_id': 21, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Female', 'breed': 'German Shepherd', 'color': 'Black'}, {'pet_name': 'Pj', 'user_id': 22, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Female', 'breed': 'Neapolitan Mastiff', 'color': 'Brindle'}, {'pet_name': 'Reuben', 'user_id': 23, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'Blue Heeler', 'color': 'Spotted, Red Merle'}, {'pet_name': 'Rex', 'user_id': 24, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'Great Pyrenees', 'color': 'White'}, {'pet_name': 'Riley', 'user_id': 25, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Female', 'breed': 'Shepherd', 'color': 'Brown'}, {'pet_name': 'Ritz', 'user_id': 26, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Female', 'breed': 'German Shepherd', 'color': 'White, Black'}, {'pet_name': 'Roo', 'user_id': 27, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'Labrador - Mix', 'color': 'White, Black'}, {'pet_name': 'Sadie', 'user_id': 28, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Female', 'breed': 'Beagle - American Pit Bull', 'color': 'White, Brown'}, {'pet_name': 'Squirm', 'user_id': 29, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'Chihuahua', 'color': 'White, Tan'}, {'pet_name': 'Tex', 'user_id': 30, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'American Pit Bull - Mix', 'color': 'White, Brindle'}, {'pet_name': 'Ursa', 'user_id': 31, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Female', 'breed': 'German Shepherd', 'color': 'Black'}, {'pet_name': 'Wednesday', 'user_id': 32, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Female', 'breed': 'Shepherd', 'color': 'White, Tan'}, {'pet_name': 'Zeus', 'user_id': 33, 'animal_type': 'dog', 'pet_type': 'rescued', 'gender': 'Male', 'breed': 'American Pit Bull', 'color': 'White, Black'}]

first_names = [
    'Jacob', 'Noah', 'Mason', 'Liam', 'William', 'Ethan', 
    'Emma', 'Sophia', 'Olivia', 'Isabella', 'Ava', 'Mia',
    'Michael', 'Alexander', 'James', 'Daniel', 'Elijah',
    'Emily', 'Abigail', 'Madison', 'Elizabeth', 'Charlotte',
    'Aiden', 'Jayden', 'Benjamin', 'Matthew', 'Logan',
    'Chloe', 'Ella', 'Amelia', 'Avery', 'Evelyn', 
]

last_names = [
    'Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Miller', 
    'Davis', 'Wilson', 'Anderson', 'Taylor', 'Garcia', 'Thomas'
]


sf_zip_codes = [94102, 94103, 94104, 94105, 94107, 94108, 94109, 94110, 94111, 94112, 94114, 94115, 94116, 94117, 94118, 94121, 94122, 94123, 94124, 94127, 94129, 94130, 94131, 94132, 94133, 94134, 94158]

def add_zip_code(list_pets, list_zc):
    new_list_pets = []
    for pet in list_pets:
        pet["zip_code"]=str(choice(list_zc))
        new_list_pets.append(pet)
    return new_list_pets

list_rescued_dogs = add_zip_code(rescued_dogs, sf_zip_codes)
#print(list_rescued_dogs)

list_rescued_cats = add_zip_code(rescued_cats, sf_zip_codes)
#print(list_rescued_cats)

i = 0
users = []
for i in range(47):
    user