import requests
from bs4 import BeautifulSoup

def get_coupons():
    # We are using the "All Deals" page which is more reliable
    url = "https://www.desidime.com/new" 
    
    # This header makes you look like a real person using Chrome
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # This is the updated "hook" for the new DesiDime layout
        deals = soup.select('a.plain-link.view-deal-main')
        
        if not deals:
            # Backup plan if the first one fails
            deals = soup.find_all('div', class_='deal-container')

        message = "🔥 Top Indian Deals Found: \n\n"
        
        # We take the top 5 deals
        count = 0
        for deal in deals:
            if count >= 5: break
            
            title = deal.get_text().strip()
            # Making sure the link is complete
            link = deal.get('href')
            if link and not link.startswith('http'):
                link = "https://www.desidime.com" + link
            
            if title and link:
                message += f"✅ {title}\n🔗 {link}\n\n"
                count += 1
        
        if count == 0:
            return "❌ No coupons found right now. The website might be blocking the bot or changed layout."
            
        return message

    except Exception as e:
        return f"⚠️ Error fetching coupons: {str(e)}"

def send_telegram(text):
    # DONT FORGET TO PUT YOUR REAL DATA HERE
    token = "8607568732:AAGihsIuxznCcnB5UGQWGt62dCwTED1ksg4" 
    chat_id = "1958886454"
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {'chat_id': chat_id, 'text': text}
    requests.post(url, data=payload)

if _name_ == "_main_":
    coupon_text = get_coupons()
    send_telegram(coupon_text)
