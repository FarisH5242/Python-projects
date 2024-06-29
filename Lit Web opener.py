import webbrowser as w

print("Here are your options for the websites that you can visit:")
print("-------")
print("tiktok")
print("youtube")
print("twitter")
print("instagram")
print("----------------------------------------------------------------------------")

website = input("What website would you like to visit")
print("Okay now opening....", website)

if website == "tiktok":
    w.open("www.tiktok.com")
if website == "twitter":
    w.open("www.twitter.com")
if website == "youtube":
    w.open("www.youtube.com")
if website == "instagram":
    w.open("www.instagram.com")

