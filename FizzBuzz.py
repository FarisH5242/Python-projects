
#FIzzBuzz machine

import math

while True:
    HelloFB = str(input("FizzBuzz MACHINE EXE. Please type you name and then press ENTER to continue"))
    fizzbuzz = int(input("Please enter a number that you would like to calculate"))
   


    if fizzbuzz %3 == 0:
        print(HelloFB,fizzbuzz,"is a Fizz")
    if fizzbuzz %5 == 0:
        print(HelloFB,fizzbuzz, "is a Buzz")
    if (fizzbuzz %5 == 0) and (fizzbuzz %3 == 0):
        print(HelloFB,"is a FizzBuzz")
    if(fizzbuzz %5 != 0) and (fizzbuzz %3 != 0):
        print(HelloFB,fizzbuzz,"is not a factor of 5 or 3")
       
       
                



