import requests
from bs4 import BeautifulSoup
import re

url = "https://lms.klh.edu.in/login/index.php"

def get_sess_key():
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    login_token = soup.find("form", class_="login-form").find("input").get("value")
    resp_cookie = response.cookies.values()[0]
    cookies = {"MoodleSession": resp_cookie}  # Corrected cookie format
    data = {'logintoken': login_token, 'username': '2210030344',
            'password': 'Aman2004@'}  # Corrected data format
    response1 = requests.post(url, cookies=cookies, data=data, allow_redirects=False)
    cookies1=[]
    for cookie in response1.cookies:
        cookies1.append(cookie.value)
    my_url="https://lms.klh.edu.in/my"
    my_cookies={'MoodleSession':cookies1[0],"MOODLEID1_":cookies1[1]}
    response2= requests.post(my_url,cookies=my_cookies ).text
    pattern = r'"sesskey":"(.*?)"'
    match = re.search(pattern,response2)
    if match:
        return match.group(1),cookies1[0],cookies1[1]
    else:
        print("Error occured")



