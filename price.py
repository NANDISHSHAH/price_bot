import requests
from bs4 import BeautifulSoup
import smtplib
URL='https://www.amazon.in/HP-Gaming-Mouse-Keyboard-GK1000/dp/B07CHBV63J/ref=sr_1_6?keywords=hp+keyboard&qid=1565415315&s=gateway&sr=8-6'
headers={"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
def check_price():
    page=requests.get(URL,headers=headers)
    soup=BeautifulSoup(page.content,'html.parser')
    title = soup.find(id="productTitle").get_text()
    price =soup.find(id="priceblock_ourprice").get_text()
    converted_price=float(price[1:5])
    if(converted_price<100):
        send_mail()
    print(converted_price)
    print(title.strip())
    if(converted_price>100):
        send_mail()
def send_mail():
    server =smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('Useremail','password')
    subject='Price Fell down!'
    body='check the amazon link:https://www.amazon.in/HP-Gaming-Mouse-Keyboard-GK1000/dp/B07CHBV63J/ref=sr_1_6?keywords=hp+keyboard&qid=1565415315&s=gateway&sr=8-6'
    msg=f"Subject:{subject}\n\n{body}"
    server.sendmail(
          'email-id',
          'email-id',
         
          msg
      )
    print("Hey Email is been sent!")
    server.quit()
check_price()
