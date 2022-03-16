

# (5 points): As a developer, I want to make at least three commits with descriptive messages. 




# (5 points): As a developer, I want to store my destinations, restaurants, mode of transportation, and entertainments in their own separate lists. 

random_locations = ['Mexico City', 'New York City', 'City of London', 'Rio de Janeiro', 'Barcelona', 'Hvar', 'Madrid', 'Berlin', 'Paris'] 
random_food = ['Happy Hour Tavern', 'Irish Deligh' , 'Gionos Pizza', 'Mama Mia Italian', 'Hola Amigos Tacos', 'Pad Thai Hour', 'Jerk Chicken Restaurant']
random_transportation = ['motorcycle', 'bicycle', 'vehicle', 'train', 'moped','electric scooter']
random_entertainment = ['movies', 'bowling', 'hiking', 'magic show', 'musical', 'music feast', 'bus tour', 'zip line']




# (5 points): As a user, I want a destination to be randomly selected for my day trip. 


import random
from tkinter import Y
from typing import final




 
def location_choice(list_of_locations):

    user_answer = 'y'

    while list_of_locations != user_answer:
        trip_location = random.choice(random_locations)
        list_of_locations = input(f'Does {trip_location} sound like a good place to visit? y/n: ')
        
        if(list_of_locations == user_answer):
            print('Excellent Choice')
            return trip_location

        print("Not a problem")
        return location_choice(random_locations)
       

chosen_location = location_choice(random_locations)


# (5 points): As a user, I want a restaurant to be randomly selected for my day trip. 

def food_choice(food):

    
    user_answer = 'y'
   
    while food != user_answer:
        food_approved = random.choice(random_food)
        food = input(f'Does {food_approved} sound like a good place to eat at? y/n: ')
        
        if(food == user_answer):
            print('Excellent Choice')
            return food_approved

        print("Not a problem")
        return food_choice(random_food)
          
approved_food = food_choice(random_food)

# (5 points): As a user, I want a mode of transportation to be randomly selected for my day trip. 

def transportation_choice(transportation):

    user_answer = 'y'
   

    while transportation != user_answer:
        transport_approved = random.choice(random_transportation)
        transportation = input(f'Does {transport_approved} sound like a good way to go around? y/n: ')
        
        if(transportation == user_answer):
            print('Excellent Choice')
            return transport_approved

        print("Not a problem")
        return transportation_choice(random_transportation)
           
    
        
            

approved_transport = transportation_choice(random_transportation)



# (5 points): As a user, I want a form of entertainment to be randomly selected for my day trip. 

def entertainment_choice(entertainment):

    
    user_answer = 'y'
   
    

    while entertainment != user_answer:
        entertainment_approved = random.choice(random_entertainment)
        entertainment = input(f'Does {entertainment_approved} sound like a fun thing to go do? y/n: ')
        
        if(entertainment == user_answer):
            print('Excellent Choice')
            return entertainment_approved

        print("Not a problem")
        return entertainment_choice(random_entertainment)
           
    
        
            

approved_entertainment = entertainment_choice(random_entertainment)


# (15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things. 

def destination_confirmation(updated_location):
    
    location = chosen_location
    updated_location = input(f'Does your original choice of location at {chosen_location} still your main choice? y/n: ')
 
    if updated_location != "y":
        print('Next choice')
        return  location_choice(random_locations)
    
    print('Perfect')
    return location

chosen_location = destination_confirmation(random_locations)

def updated_food_choice(food_approved):
    food = approved_food
    food_approved = input(f'Does your original choice of food at {approved_food} still your main choice? y/n: ')
 
    if food_approved != "y":
        print('Next choice')
        return  food_choice(random_food)
    
    print('Perfect')
    return food

approved_food = updated_food_choice(random_food)

def updated_transportation_choice(transportation):
    transport = approved_transport
    transportation = input(f'Does your original choice of transportation {approved_transport} still your main choice? y/n: ')
 
    if transportation != "y":
        print('Next choice')
        return  transportation_choice(random_transportation)
    
    print('Perfect')
    return transport

approved_transport = updated_transportation_choice(random_transportation)

def updated_entertainment_choice(entertainment):

    final_entertainment = approved_entertainment
    entertainment = input(f'Does your original choice of entertainment {approved_entertainment} still your main choice? y/n: ')
 
    if entertainment != "y":
        print('Next choice')
        return  entertainment_choice(random_entertainment)
    
    print('Perfect')
    return final_entertainment

approved_entertainment = updated_entertainment_choice(random_entertainment)


# (10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections. 

def confirmation():
  print("These are the locations you picked")
confirmation()

def destination_confirmation(updated_location):
    
    location = chosen_location
    updated_location = input(f'Location {location} confirmed: Press Enter')
 
    if updated_location == "":
        return location
    
chosen_location = destination_confirmation(random_locations)

def updated_food_choice(food_approved):
    food = approved_food
    food_approved = input(f'Food {food} confirmed: Press Enter')
 
    if food_approved == "":
        return food
    
    
approved_food = updated_food_choice(random_food)

def updated_transportation_choice(transportation):
    transport = approved_transport
    transportation = input(f'Transportation {transport} confirmed: Press Enter')
 
    if transportation == "":
        return  transport
    
approved_transport = updated_transportation_choice(random_transportation)

def updated_entertainment_choice(entertainment):

    final_entertainment = approved_entertainment
    entertainment = input(f'Entertainment {final_entertainment} confirmed: Press Enter')
 
    if entertainment == "":
       return  final_entertainment

approved_entertainment = updated_entertainment_choice(random_entertainment)



 
   




# (10 points): As a user, I want to display my completed trip in the console. 

def confirmation():
  print("This is your complete trip")
confirmation()


def destination_confirmation(updated_location):
    
    location = chosen_location
    updated_location = (f'You are going to {location}')
 
    if updated_location == "":
        return location
    print(location)
    
chosen_location = destination_confirmation(random_locations)

def updated_food_choice(food_approved):
    food = approved_food
    food_approved = (f'You are eating at {food}')
 
    if food_approved == "":
        return food
    print(food_approved)
approved_food = updated_food_choice(random_food)

def updated_transportation_choice(transportation):
    transport = approved_transport
    transportation = (f'You are moving on {transport}')
 
    if transportation == "":
        return  transport
    print(transportation)
approved_transport = updated_transportation_choice(random_transportation)

def updated_entertainment_choice(entertainment):

    final_entertainment = approved_entertainment
    entertainment = (f'This is what you are doing {final_entertainment}')
 
    if entertainment == "":
       return  final_entertainment
    print(entertainment)
approved_entertainment = updated_entertainment_choice(random_entertainment)


# (5 points): As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing!






