#Exchange rate converter

from time import sleep


display = print

print("")
print("Lix Exchange rate Converter")
print("Here is list of currencies we can convert")
print("-british pounds , pounds")
print("-euros , euros")
print("-american dollars , dollars")
print("-saudi riyals , riyals")
print("-----------------")

choose_first_converter = str(input("Please enter your first currency[This will be converted into second currency]"))
choose_second_converter = str(input("Please enter your second currency"))

ask_which_convert = float(input("How much of your first currency  would you like to be converted into your second currency"))





def british_pounds():
    if choose_first_converter == "pounds" and choose_second_converter == "euros":
        print(ask_which_convert*1.9)
        
    if choose_first_converter == "pounds" and choose_second_converter == "dollars":
        print(ask_which_convert *1.3)

    if choose_first_converter == "pounds" and choose_second_converter == "riyals":
        print(ask_which_convert *5.02)


def euros():
    if choose_first_converter == "euros" and choose_second_converter == "pounds":
        print(ask_which_convert*0.84)
        
    if choose_first_converter == "euros" and choose_second_converter == "dollars":
        print(ask_which_convert *1.12)

    if choose_first_converter == "euros" and choose_second_converter == "riyals":
        print(ask_which_convert *4.22) 

def dollars():
    if choose_first_converter == "dollars" and choose_second_converter == "pounds":
        print(ask_which_convert*0.75)
        
    if choose_first_converter == "dollars" and choose_second_converter == "euros":
        print(ask_which_convert *0.89)

    if choose_first_converter == "dollars" and choose_second_converter == "riyals":
        print(ask_which_convert *3.75)
        
def riyals():
    if choose_first_converter == "riyals" and choose_second_converter == "pounds":
        print(ask_which_convert*0.20)
        
    if choose_first_converter == "riyals" and choose_second_converter == "euros":
        print(ask_which_convert *0.24)

    if choose_first_converter == "riyals" and choose_second_converter == "dollars":
        print(ask_which_convert *0.27)
 
british_pounds()
euros()
dollars()
riyals()
