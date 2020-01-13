from bs4 import BeautifulSoup
import ssl
import json
from urllib.request import Request, urlopen


if __name__== '__main__':
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = input("Enter YouTube Video URL: ")

    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()

    soup = BeautifulSoup(webpage, 'html.parser')
    video_details = {}

    for span in soup.findAll('span', attrs={'class': 'watch-title'}):
        video_details['TITLE'] = span.text.strip()

    for script in soup.findAll('script', attrs={'type': 'application/ld+json'}):
        channelDescription = json.loads(script.text.strip())
        video_details['CHANNEL_NAME'] =channelDescription['itemListElement'][0]['item']['name']

    for div in soup.findAll('div', attrs={'class': 'watch-view-count'}):
        video_details['NUMBER_OF_VIEWS'] = div.text.strip()

    for button in soup.findAll('button', attrs={'title': 'I like this'}):
        video_details['LIKES'] = button.text.strip()

    for button in soup.findAll('button', attrs={'title': 'I dislike this'}):
        video_details['DISLIKES'] = button.text.strip()

    for span in soup.findAll('span', attrs={'class': 'yt-subscription-button-subscriber-count-branded-horizontal yt-subscriber-count'}):
        video_details['NUMBER_OF_SUBSCRIPTIONS'] = span.text.strip()

    with open('data.json', 'w', encoding='utf8') as outfile:
        json.dump(video_details, outfile, ensure_ascii=False, indent=4)

    print('------Extraction of data is complete. Check json file.------')

    # DO THE BONUS

