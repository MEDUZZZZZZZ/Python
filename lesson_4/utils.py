import requests
import datetime
def currency_rates(valute, url = 'http://www.cbr.ru/scripts/XML_daily.asp'):
    response = requests.get(url)
    encodings = requests.utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    name = valute.upper()
    value = None
    if name in content:
        content_2 = content[content.find(name):]
        start_index = content_2.find('<Value>') + len('<Value>')
        stop_index = content_2.find('</Value>')
        value = float((content_2[start_index:stop_index].replace(',', '.')))
    return value

def currency_rates_adv(valute, url = 'http://www.cbr.ru/scripts/XML_daily.asp'):
    response = requests.get(url)
    encodings = requests.utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    name = valute.upper()
    value = None
    start_index = content.find('Date="') + len('Date="')
    stop_index = content.find('" name')
    date, mounth, year = content[start_index: stop_index].split('.')
    today_date = datetime.date(year = int(year), month = int(mounth), day = int(date))
    if name in content:
        content = content[content.find(name):]
        start_index = content.find('<Value>') + len('<Value>')
        stop_index = content.find('</Value>')
        value = float((content[start_index:stop_index].replace(',', '.')))
    return today_date, value


if __name__ == '__main__':
    print('Тест функции currency_rates')
    print(currency_rates('uSD'))
    print(currency_rates('HUF'))
    print(currency_rates('OLeg'))
    print('Тест функции currency_rates_adv')
    print(currency_rates_adv('uSD'))
    print(currency_rates_adv('HUF'))
    print(currency_rates_adv('OLeg'))