from bs4 import BeautifulSoup
import ssl
import json
import csv
from urllib.request import Request, urlopen

allVideos = {}


def parse_video_from_url(url, iterationNum=0):
    global allVideos

    iteration = "" if iterationNum == 0 else " #" + str(iterationNum+1)

    print("Examining Video" + iteration)

    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()

    soup = BeautifulSoup(webpage, 'html.parser')
    video_details = {}

    for span in soup.findAll('span', attrs={'class': 'watch-title'}):
        video_details['TITLE'] = span.text.strip()

    for script in soup.findAll('script', attrs={'type': 'application/ld+json'}):
        channelDescription = json.loads(script.text.strip())
        video_details['CHANNEL_NAME'] = channelDescription['itemListElement'][0]['item']['name']

    for div in soup.findAll('div', attrs={'class': 'watch-view-count'}):
        video_details['NUMBER_OF_VIEWS'] = div.text.strip()

    for button in soup.findAll('button', attrs={'title': 'I like this'}):
        video_details['LIKES'] = button.text.strip()

    for button in soup.findAll('button', attrs={'title': 'I dislike this'}):
        video_details['DISLIKES'] = button.text.strip()

    for span in soup.findAll('span', attrs={'class': 'yt-subscription-button-subscriber-count-branded-horizontal yt-subscriber-count'}):
        video_details['NUMBER_OF_SUBSCRIPTIONS'] = span.text.strip()

    with open('data.json', 'w', encoding='utf8') as outfile:
        # json.dump(video_details, outfile, ensure_ascii=False, indent=4)
        allVideos[iterationNum] = video_details
        json.dump(allVideos, outfile, ensure_ascii=False, indent=4)

    print('------Extraction of data is complete. Check json file.------\n')


def read_json_file():
    with open('data.json') as fp:
        line = fp.readline()
        while line:
            print(line)
            line = fp.readline()


def csv_to_array(file_path):
    with open(file_path, newline='') as csvfile:
        data = list(csv.reader(csvfile))
    return data


def exit_options():
    ans = input("\nDo you want to:\n1) Print out JSON file\n2) Exit Program\n~")
    if ans == "1":
        read_json_file()
    else:
        print("Exiting Program.")
        quit()


if __name__ == '__main__':
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    version = input("\nDo you want to:\n1) Enter a YouTube URL\n2) Enter a .CSV of YouTube URLS\n~")

    notSet = True
    while notSet:
        if version == "1":
            notSet = False
            url = input("\nEnter YouTube Video URL: ")

            parse_video_from_url(url)
            exit_options()

        elif version == "2":
            notSet = False

            path = input("\nEnter CSV file path: ")

            array = csv_to_array(path)

            count = 0
            for subArray in array:
                for url in subArray:
                    parse_video_from_url(url, count)
                    count += 1

            exit_options()

        else:
            print("Try again")

