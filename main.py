import datetime
from requests import Session
import json
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects


url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'


def get_price(link):
    """send req to api for a dict of crypto names and prices

    Args:
        link (str): api link

    Returns:
        a dict wit names: * & price: ** and time : ***
    """

    parameters = {
        'start': '1',
        'limit': '20',
        'convert': 'USD'
    }

    head = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': "API KEY"

    }

    session = Session()
    session.headers.update(head)
    names_price_dict = dict()
    try:

        # try to send a get req with your api key

        res = session.get(url=link, params=parameters)
        result = json.loads(res.text)
        for i in result['data']:
            price = i['quote']['USD']['price']
            name = i['name']
            names_price_dict[name] = price

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

    return names_price_dict


def msg():
    a = ''
    name_price_dic = get_price(url)

    names = name_price_dic.keys()

    for i in names:
        a += f'Crypto name is : "{i}" & Price : ({round(name_price_dic[i], 4)}$)\tdate : {datetime.datetime.now()}\n'
    return a
