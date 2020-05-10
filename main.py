import requests
from bs4 import BeautifulSoup
import datetime
textNews = []
linkNews = []
newsDone = ''
while True:
    time.sleep(1800)
    now = datetime.datetime.now()
    if str(now.hour):
        URL = '' #fill with your weather.com location link
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')

        temp=soup.find("div",{"class":"today_nowcard-temp"}).find("span").text
        sky = soup.find("div",{"class":"today_nowcard-phrase"}).text
        feels = soup.find("span",{"class":"deg-feels"}).text
        prob = soup.find("span",{"class":"precip-val"}).text

        URL = 'https://www.ansa.it/sito/notizie/topnews/index.shtml' #italian news website
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        news = soup.find_all("h3",{"class":"news-title"})
        counter = 0
        while counter < 6:
            textNews.append(news[counter].text)
            tempVar = news[counter].find("a")
            linkNews.append(tempVar["href"])
            counter += 1
        counter = 0
        while counter < 6:
            hyperLinkLink = "https://www.ansa.it/" + str(linkNews[counter])
            hyperLinkText = str(textNews[counter])
            newsDone = newsDone + "[" + hyperLinkText + "]" + "(" +hyperLinkLink + ")" + "\n\n"
            counter += 1


        #This is the message sent by the bot, obv you can change it and adapt it for your language
        string = "Buongiorno,\n la temperatura esterna é di " + temp + ", percepita: " +  feels + "\nIl cielo é " + sky.lower() + " con probabilitá di pioggia di " + prob
        string = string + "\n\n" + "**Ecco le ultime notizie**\n" + newsDone

        def telegram_bot_sendtext(bot_message):
            bot_token = '' #insert your bot token here
            bot_chatID = '' #insert your chat id here
            send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

            response = requests.get(send_text)

            return response.json()


        test = telegram_bot_sendtext(string)
        print(test)


