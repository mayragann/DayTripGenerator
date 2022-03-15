

# (5 points): As a developer, I want to make at least three commits with descriptive messages. 




# (5 points): As a developer, I want to store my destinations, restaurants, mode of transportation, and entertainments in their own separate lists. 

random_locations = ['Mexico City', 'New York City', 'City of London', 'Rio de Janeiro', 'Barcelona', 'Hvar', 'Madrid', 'Berlin', 'Paris'] 
random_food = ['Happy Hour Tavern', 'Irish Deligh' , 'Gionos Pizza', 'Mama Mia Italian', 'Hola Amigos Tacos', 'Pad Thai Hour', 'Jerk Chicken Restaurant']
random_transportation = ['motorcycle', 'bicycle', 'vehicle', 'train', 'moped','electric scooter']
random_entertainment = ['movies', 'bowling', 'hiking', 'magic show', 'musical', 'music feast', 'bus tour', 'zip line']




# (5 points): As a user, I want a destination to be randomly selected for my day trip. 


import random



def location_choice(list_of_locations):

    user_answer = 'y'
    
    while list_of_locations != user_answer:
        trip_location = random.choice(random_locations)
        list_of_locations = input(f'Does {trip_location} sound like a good place to visit? y/n: ')
        if list_of_locations != user_answer:
            print("Not a problem")
        else:
            print('Excellent Choice')

location_choice(random_locations)
        
# (5 points): As a user, I want a restaurant to be randomly selected for my day trip. 

def food_choice(food_locations):

    user_answer = 'y'
    
    while food_locations != user_answer:
        restaurant= random.choice(random_food)
        food_locations = input(f'Does {restaurant} sound like a good place eat at? y/n: ')
        if food_locations != user_answer:
            print("Let's try something different")
        else:
            print('Sounds Delicious!!')

food_choice(random_food)

# (5 points): As a user, I want a mode of transportation to be randomly selected for my day trip. 

def transportation_choice(transportation):

    user_answer = 'y'
    
    while transportation != user_answer:
        mode_of_transport= random.choice(random_transportation)
        transportation = input(f'Does {mode_of_transport} sound like a good way to get around? y/n: ')
        if transportation != user_answer:
            print("Let's try again")
        else:
            print('Sounds fun!!')

transportation_choice(random_transportation)



# (5 points): As a user, I want a form of entertainment to be randomly selected for my day trip. 

def entertainment_choice(entertainment):

    user_answer = 'y'
    
    while entertainment != user_answer:
        mode_of_entertainment= random.choice(random_entertainment)
        entertainment = input(f'Does {mode_of_entertainment} sound like a good way to get around? y/n: ')
        if entertainment != user_answer:
            print("Let's try again")
        else:
            print('Sounds fun!!')

entertainment_choice(random_entertainment)


# (15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things. 




# (10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections. 





# (10 points): As a user, I want to display my completed trip in the console. 
# (5 points): As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing!






