import webbrowser as w
from time import sleep

print("-------------------------------------------------------")
print("➤ Welcome to the Litopener - the number 1 Software and app opener")
print("-------------------------------------------------------")
print("3 levels for opening apps - Level 1, Level 2, Level 3")
print("Open up to 5 apps without paying")
print("Free and stable for all platforms")
print("-------------------------------------------------------")
print("Bugs and issues")
print("Level 2 & 3 -  are currently not availble")
print("-------------------------------------------------------")
print("Here are the 5 websites that you can open with Level 1")
print("-Instagram")
print("-Twitter")
print("-tiktok")
print("-Whatsapp")
print("-twitch")
print("-------------------------------------------------------")


open_question = input(str("Would you like to open a website/app"))
if open_question == "Yes" or open_question == "yes":
    print("."); sleep (0.3)
    print(".."); sleep(0.5)
    print("..."); sleep(0.7)
    web_question = input("Enter a website that you would like to open from the list -")
    if web_question == "instagram" or web_question == "Instagram":
        w.open("instagram.com")
    if web_question == "Twitter" or web_question == "twitter":
        w.open("twitter.com")
    if web_question == "tiktok" or web_question == "Tiktok":
        w.open("tiktok.com")
    if web_question == "Whatsapp" or web_question == "whatsapp":
        w.open("webwhatsapp.com")
    if web_question == "twitch" or web_question == "Twitch":
        w.open("twitch.com")


print("-----------------------------------")
if open_question == "no" or open_question == "No":
    print("Okay ty for using litopener")
    
    


  
