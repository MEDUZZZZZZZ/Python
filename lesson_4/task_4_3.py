import datetime
import requests

def currency_rates_adv(Valute, url = 'http://www.cbr.ru/scripts/XML_daily.asp'):
    response = requests.get(url)
    encodings = requests.utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    name = Valute.upper()
    value = None
    start_index = content.find('Date="') + len('Date="')
    stop_index = content.find('" name')
    date, month, year = content[start_index: stop_index].split('.')
    today_date = datetime.date(year = int(year), month = int(month), day = int(date))
    if name in content:
        content = content[content.find(name):]
        start_index = content.find('<Value>') + len('<Value>')
        stop_index = content.find('</Value>')
        value = float((content[start_index:stop_index].replace(',', '.')))
    return today_date, value

if __name__ == '__main__':
    print(currency_rates_adv('uSD'))
    print(currency_rates_adv('HUF'))
    print(currency_rates_adv('OLeg'))