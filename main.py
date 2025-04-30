import feedparser
import time
import telegram

BOT_TOKEN = "7595803112:AAEPY6RHMoHE5cPpwxbRVCZKy3Kwrd9k0Fw"
CHAT_ID = "1649212096"
RSS_FEEDS = [
    "https://nitter.privacydev.net/krnl_xyz/rss",
    "https://nitter.privacydev.net/asim_eth/rss",
    "https://nitter.privacydev.net/tahir_mahmood/rss"
]

posted_links = set()
bot = telegram.Bot(token=BOT_TOKEN)

def check_feeds():
    for url in RSS_FEEDS:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            if entry.link not in posted_links:
                posted_links.add(entry.link)
                bot.send_message(chat_id=CHAT_ID, text=entry.link)

while True:
    check_feeds()
    time.sleep(60)
