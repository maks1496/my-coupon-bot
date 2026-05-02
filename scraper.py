import requests
from bs4 import BeautifulSoup

def get_coupons():
    # Switching to GrabOn (Trending Deals) - Very reliable for India
    url = "https://www.grabon.in/" 
    
    # These headers make the bot look like a real person using a laptop
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
        'Referer': 'https://www.google.com/'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        if response.status_code != 200:
            return f"❌ Website blocked the bot (Error {response.status_code})"

        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Finding the 'Trending' deal cards on GrabOn
        deals = soup.select('div.home-trending-offers-list li')
        
        message = "🇮🇳 Top Indian Coupons Found: \n\n"
        
        count = 0
        for deal in deals:
            if count >= 6: break
            
            # Extracting Title and Link
            link_tag = deal.find('a')
            if link_tag:
                title = link_tag.get('title') or link_tag.text.strip()
                link = link_tag.get('href')
                
                if not link.startswith('http'):
                    link = "https://www.grabon.in" + link
                
                message += f"🎁 {title}\n🔗 {link}\n\n"
                count += 1
        
        if count == 0:
            return "⚠️ Found the website, but couldn't find specific deal boxes. The layout might have changed."
            
        return message

    except Exception as e:
        return f"⚠️ Technical Error: {str(e)}"

def send_telegram(text):
    # --- ENTER YOUR DATA HERE ---
    token = "8607568732:AAGihsIuxznCcnB5UGQWGt62dCwTED1ksg4" 
    chat_id = "1958886454"
    # ----------------------------
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {'chat_id': chat_id, 'text': text}
    try:
        requests.post(url, data=payload)
    except:
        pass

if _name_ == "_main_":
    coupon_text = get_coupons()
    send_telegram(coupon_text)
