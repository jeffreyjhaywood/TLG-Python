import requests
import wget

date = input("Enter date of NASA picture you'd like (YYYY-MM-DD)")

# Variable used to check that the date is less than API start date
date_check = date.replace("-", "")

if date[0 : 4] == "2552":
    wget.download("https://content.halocdn.com/media/Default/games/halo-combat-evolved/media/hce_010-31fd86b7173d4ab6ad8df20c98fac7bd.jpg")

elif int(date_check) > 19950616:
    url = "https://api.nasa.gov/planetary/apod?date="
    image_quality = int(input("What quality would you like?\n1. HD\n2. Standard"))

    key = "GeUewdFsXc3skmEKsMEKRWPsQJHPwpWYTLrm1eNY"
    full_url = url + date + "&api_key="  + key
    nasa_response = requests.get(full_url).json()

    print(nasa_response)

    title = nasa_response["title"]
    explanation = nasa_response["explanation"]
    
    if image_quality == 1:
        wget.download(nasa_response["hdurl"])

    else:
        wget.download(nasa_response["url"])



else:
    print("Cannot get images prior to 1995-06-16")
