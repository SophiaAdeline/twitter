import os
import tweepy
import google.generativeai as genai
import json
import time

# Load config
with open('config.json') as f:
    config = json.load(f)

# Autentikasi Twitter
auth = tweepy.OAuthHandler(os.getenv('TWITTER_API_KEY'), os.getenv('TWITTER_API_SECRET'))
auth.set_access_token(os.getenv('TWITTER_ACCESS_TOKEN'), os.getenv('TWITTER_ACCESS_TOKEN_SECRET'))
api = tweepy.API(auth)

# Autentikasi Gemini
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

def get_trending_hashtags():
    """Ambil hashtag trending dari Twitter"""
    trends = api.get_place_trends(id=config['country_code'])[0]['trends']
    return [t['name'] for t in trends if t['name'].startswith('#')][:config['max_hashtags']]

def generate_content():
    """Buat konten tweet menggunakan Gemini"""
    prompt = f"""
    Buatlah tweet tentang {config['link']} dengan:
    - Bahasa: {config['language']}
    - Panjang maksimal 250 karakter
    - Sertakan emoji relevan
    - Jangan tambahkan hashtag
    """
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text.strip()

def post_tweet():
    """Posting tweet ke Twitter"""
    content = generate_content()
    hashtags = " ".join(get_trending_hashtags())
    
    tweet = f"{content}\n\n{config['link']}\n{hashtags}"
    api.update_status(tweet[:280])  # Pastikan tidak melebihi batas karakter

if __name__ == "__main__":
    post_tweet()
