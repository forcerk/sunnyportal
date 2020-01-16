from bs4 import BeautifulSoup
import requests

payload = {
    'inUserName': 'boettcher.erik@gmail.com',
    'inUserPass': 'password'
}

url = "https://www.sunnyportal.com/Templates/Login.aspx"

# Use 'with' to ensure the session context is closed after use.
with requests.Session() as session:
    login = session.post(url, data=payload)
    print(login.status_code)

    # An authorised request.
    #request = session.get('https://www.sunnyportal.com/FixedPages/HoManLive.aspx')
    #soup = BeautifulSoup(request.content, 'html.parser')
    #print(soup)
    """spans = soup.find_all('span', attrs={'class':'batteryStatus-value h3 header'})
    for span in spans:
            print(span.string)"""
    print(session)