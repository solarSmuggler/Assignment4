# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 08:45:36 2022

@author: Kassaundra
"""

# Conditionals

response = "1"
if response == "1" or response == "2" :
    print("OK") 
    if response == "1" :
        print("Correct")
    elif response == "2" :
       print("Incorrect") 
    
elif response == "NaN" :
    print("subject did not respond")
    
else :
    print("subject pressed the wrong key")
# it does what i expect

# For Loops

name = "Kassaundra"
name_count = -1
for i in name:
    name_count = name_count+1
    letter = i
    print(letter, name_count)

people = ["Amy", "River","Rory"]
for person in people :
    people_count = -1
    for index in person :
        people_count = people_count+1
        print(index, people_count)
        
# While Loop
iteration = 1
while iteration <= 20 :
    if iteration <= 10 :
        print("image1.png")
        iteration = iteration+1
    if iteration > 10 and iteration <= 20 :
        print("image2.png")
        iteration = iteration+1
  
failsafe = -1
key_response = "NaN"
while key_response == "NaN" :
    failsafe = failsafe+1
    if failsafe == 5 :
        break
    print("image")
   
    
