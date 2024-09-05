# -*- coding: utf-8 -*-
"""
Author: Haris Jafri
"""

def password_valid(password): #creating a function password_valid to check whether password is strong or not
    number_of_digits = 0
    number_of_special_characters = 0
    special_characters = ['!', '@', '#', '$', '%', '&', '*']
    for x in password:
        if x.isnumeric():
            number_of_digits += 1
    for x in password:
        if x in special_characters:
            number_of_special_characters += 1
    if len(password)>=7 and number_of_digits>=2 and number_of_special_characters>=2:
        return "Strong"
    else:
        return "Weak"

pw = input("Input Your Password here: -->")

print("The Password you input is",password_valid(pw)+".")