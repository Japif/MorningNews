import requests
import json


def telegram_bot_sendtext(bot_message):
    bot_token = ''  # insert your bot token here
    bot_chatID = ''  # insert your chat id here
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    r = requests.get(send_text)
    return r.json()


OWM_API_KEY = "" # insert your OpenWeatherMap api key here
LATITUDE = "" # insert your latitude here
LONGITUDE = "" # insert your longitude here
newsdata = False
weatherdata = False
weatherurl = f"https://api.openweathermap.org/data/2.5/weather?lat={LATITUDE}&lon={LONGITUDE}&units=metric&appid={OWM_API_KEY}"
r = requests.get(weatherurl)
if r.status_code == 200:
    weatherdata = r.json()

r = requests.get("https://www.bbc.com/news/world")
if r.status_code == 200:
    newsdata = json.loads(r.text.split("['index-page'] = ")[1].split(";\n</script>")[0])

if newsdata and weatherdata:
    string = f"Good morning,\nThe temperature outside is {weatherdata['main']['temp']}°C, feels like: {weatherdata['main']['feels_like']}°C\nThe sky condition is {weatherdata['weather'][0]['description']}"
    news = ""
    for item in newsdata["topStories"]["stories"]["items"]:
        news = news + f"[{item['title']}](https://www.bbc.com{item['url']}) \n"
    string = string + "\n\n" + "**The last news from the world:**\n" + news
    telegram_bot_sendtext(string)
else:
    print("There was an error")