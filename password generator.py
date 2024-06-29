#random password generator
#under 10 minutes

import random


alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def password_generation():
    password_former = random.sample((alpha),8)
    print(password_former)

password_generation()



    

