#Golf by Faris hamdani


from time import sleep

#Number of players
number_ofplayers = int(input("How many players are taking part?"))

#Names of the players
if number_ofplayers == 1:
    name__ofplayers1 = input("enter your name")
if number_ofplayers == 2:
    name__ofplayers2 = input("enter your names")
    name__ofplayers2_1 = input("enter your names")
if number_ofplayers == 3:
    name__ofplayers3 = input("enter your names")
    name__ofplayers3_1 = input("enter your names")
    name__ofplayers3_2 = input("enter your names")
if number_ofplayers == 4:
    name__ofplayers4 = input("enter your names")
    name__ofplayers4_1 = input("enter your names")
    name__ofplayers4_2 = input("enter your names")
    name__ofplayers4_3 = input("enter your names")


#Number of holes
number_ofholes = int(input("How many holes will you be playing, 9/18"))

#par of the whole course
par_ofcourse = "80"


#Storing the names in a list
mylist = []
if number_ofplayers == 1:
    mylist.insert(0,name__ofplayers1)

if number_ofplayers == 2:
    mylist.insert(0,name__ofplayers2)
if number_ofplayers == 2:
    mylist.insert(1,name__ofplayers2_1)

if number_ofplayers == 3:
    mylist.insert(0,name__ofplayers3)
if number_ofplayers == 3:
    mylist.insert(1,name__ofplayers3_1)
if number_ofplayers == 3:
    mylist.insert(2,name__ofplayers3_2)

if number_ofplayers == 4:
    mylist.insert(0,name__ofplayers4)
if number_ofplayers == 4:
    mylist.insert(1,name__ofplayers4_1)
if number_ofplayers == 4:
    mylist.insert(2,name__ofplayers4_2)
if number_ofplayers == 4:
    mylist.insert(3,name__ofplayers4_3)
#----------------------------------------------------------------------------------------------------------------------
print(".");sleep(0.3)
print("..");sleep(0.5)
print("...");sleep(0.7)

print("The number of holes you will be playing is - ",number_ofholes)
print("the par of this course is",par_ofcourse)
print("The number of players are",number_ofplayers)
print("The names registered are",mylist)


