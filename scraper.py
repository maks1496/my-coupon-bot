import requests
from bs4 import BeautifulSoup

# This finds the coupons
def get_coupons():
    url = "https://www.desidime.com/categories/coupons"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    deals = soup.find_all('div', class_='deal-container', limit=5)
    message = "🔥 Top Coupons Found Today: \n\n"
    
    for deal in deals:
        title = deal.find('a', class_='deal-title').text.strip()
        link = "https://www.desidime.com" + deal.find('a')['href']
        message += f"✅ {title}\n🔗 Link: {link}\n\n"
    
    return message

# This sends the message to your phone
def send_telegram(text):
    token = "8607568732:AAGihsIuxznCcnB5UGQWGt62dCwTED1ksg4"
    chat_id = "1958886454"
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}"
    requests.get(url)

if __name__ == "__main__":
    coupon_text = get_coupons()
    send_telegram(coupon_text)
