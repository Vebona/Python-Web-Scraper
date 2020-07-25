#App to track price of sony a7 on amazon and send a notification email when the price drops below a certain amount.
# step 1. on terminal install requests and bs4 with code: 
# pip install requests bs4

#allows us to access url and pull out the data from that website  
import requests

import smtplib 

# beautiful soup allows us to parsethe data we have returned from the url 
# and pull out individual items from it
from bs4 import BeautifulSoup

#this is the url we want to pull data from
URL = 'https://www.amazon.com/Sony-Mirrorless-Digital-Camera-28-70mm/dp/B00PX8CNCM/ref=sr_1_3?dchild=1&keywords=sony+A7&qid=1595620726&sr=8-3'

# this is a dictionary. User-Agent gives us information about our browser
headers = {"user-Agent" : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15'}

def check_price():

    #make a call using get() function. This will return all the data from the website
    page = requests.get(URL, headers = headers)

    # html.parser will parse the information for us and allow us to pull out
    # individual pieces of information
    soup = BeautifulSoup(page.content, "html.parser")

    # this will allow us see what we have pasrsed
    """print(soup.prettify())"""

    title = soup.find(id ="productTitle").get_text()

    price = soup.find(id = "priceblock_ourprice").get_text()
    converted_price = float(price[0:5])

    if converted_price < 1.700 :
        send_mail()

    print(converted_price)
    print(title.strip())

    if converted_price > 1.700:
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    # first argument is username, second is password
    server.login('username@gmail.com', 'password')

    subject = 'Price fell down!'

    body = 'Check the amazon link https://www.amazon.com/Sony-Mirrorless-Digital-Camera-28-70mm/dp/B00PX8CNCM/ref=sr_1_3?dchild=1&keywords=sony+A7&qid=1595620726&sr=8-3'

    msg = f"Subject: {subject}\n\n{body}"
    
    # first argument is email I'm sending from, second argument is the email I'm sending the message to
    server.sendmail(
        'sentfrom@gmail.com',
        'sentto@gmail.com',
        msg
    )

    print('HEY EMAIL HAS BEEN SENT!')

    server.quit()

check_price()




