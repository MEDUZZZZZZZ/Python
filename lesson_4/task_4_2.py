import requests
def currency_rates(valute, url = 'http://www.cbr.ru/scripts/XML_daily.asp'):
    response = requests.get(url)
    encodings = requests.utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    valute = valute.upper()
    if valute in content:
        content_2 = content[content.find(valute):]
        start_index = content_2.find('<Value>') + len('<Value>')
        stop_index = content_2.find('</Value>')
        value = float((content_2[start_index:stop_index].replace(',', '.')))
        return value

if __name__ == '__main__':
    print(currency_rates('uSD'))
    print(currency_rates('HUF'))
    print(currency_rates('OLeg'))






