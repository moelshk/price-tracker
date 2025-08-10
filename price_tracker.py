import requests  # pip install requests
from bs4 import BeautifulSoup  # pip install bs4
import smtplib

URL = 'https://www.amazon.co.uk/Sony-ILCE7SM3B-CEC-A7S-III/dp/B08PMH2DN5/ref=sr_1_1?crid=2XNZAW3CZKDWW&keywords=sony+a7siii&qid=1684429084&sprefix=sony+a7sii%2Caps%2C362&sr=8-1'

headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}


def CheckPrice():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id="productTitle").get_text()
    price = soup.find(class_="a-price-whole").get_text()
    converted_price = float(price.replace(',', ''))

    if (converted_price > 4000):
        send_mail()

    print(title)
    print(converted_price)

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()


    server.login('elsheikhmoha@gmail.com', 'yctwozlqcmirpxjn')

    subject = 'Price fell down!'
    body = 'Check the amazon link https://www.amazon.co.uk/Sony-ILCE7SM3B-CEC-A7S-III/dp/B08PMH2DN5/ref=sr_1_1?crid=2XNZAW3CZKDWW&keywords=sony+a7siii&qid=1684429084&sprefix=sony+a7sii%2Caps%2C362&sr=8-1'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        [email_from],
        [email_to],
        msg 
    )
    print('EMAIL HAS BEEN SENT!')

    server.quit()

CheckPrice()
