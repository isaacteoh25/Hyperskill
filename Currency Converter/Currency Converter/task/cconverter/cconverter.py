# # write your code here!
# # print("Please, enter the number of conicoins you have:")
# # coin = float(input())
# import json
#
# import requests
#
# # cache = {'http://www.floatrates.com/daily/usd.json', 'http://www.floatrates.com/daily/eur.json'}
# # cache =dict()
# cache ={'eur': { 'rate': 0.82780741754765}, 'usd':{'rate': 0.30661120978056}}
#
# def get_currency_from_server(url):
#     # print("Fetching article from server...")
#     json_to_be= requests.get(url)
#     return json_to_be.text
#
# def get_currency(url,rec):
#     # print("Getting article...")
#     if rec not in cache:
#         print("Sorry, but it is not in the cache!")
#         cache[rec] = json.loads(get_currency_from_server(url))[rec.lower()]
#     else:
#         print("Oh! It is in the cache!")
#         cache[rec] = json.loads(get_currency_from_server(url))[rec.lower()]
#     return cache[rec]
# # coin = 10
# # print("Please, enter the exchange rate:")
# # ex =  float(input())
# # print(f"The total amount of dollars: {coin * ex}")
# # print(f"""
# # I will get {coin * 2.98 } RUB from the sale of {coin} conicoins.
# # I will get {coin * 0.82} ARS from the sale of {coin} conicoins.
# # I will get {coin * 0.17} HNL from the sale of {coin} conicoins.
# # I will get {coin * 1.9622} AUD from the sale of {coin} conicoins.
# # I will get {coin * 0.208} MAD from the sale of {coin} conicoins.""")
# # inputs = [['usd', 'eur', '20', 'nok', '45', 'sek', '75',  'nok', '55', 'isk', '91', ''],
# #                   ['rub', 'jpy', '80', 'jpy', '95', ''],
# #                   ['ils', 'usd', '45', 'rsd', '57', 'eur', '33', ''],
# #                   ['cad', 'dkk', '15', 'gel', '35', 'mkd', '41', '']]
# curr = input()
# while True:
#     rec = input()
#     if rec.strip() == '':
#         break
#     mon = float(input())
#     # for i in range(0, len(inputs)):
#     print("Checking the cache…")
#     # json_to_be= requests.get(f'http://www.floatrates.com/daily/{curr.lower()}.json').text
#     # print(r)
#     # print(r.text)
#     # cur_json = json.loads(get_currency(f'http://www.floatrates.com/daily/{inputs[i][0].lower()}.json'))[inputs[i][1].lower()]['rate']
#     # if curr == 'usd' or curr =='eur' or rec =='usd'or rec =='eur':
#     #     url = f'http://www.floatrates.com/daily/{curr.lower()}.json'
#     #     cache[url] = requests.get(url).text
#     #     cur_json = json.loads(cache[url])[rec.lower()]['rate']
#     #     print("Oh! It is in the cache!")
#     # else:
#     cur_json = get_currency(f'http://www.floatrates.com/daily/{curr.lower()}.json', rec)['rate']
#     # eur_json = json.loads(get_currency(f'http://www.floatrates.com/daily/{curr.lower()}.json'))['eur']
#     # print(cur_json * mon)
#     print(f"You received {round(cur_json * mon, 2)} {rec.upper()}.")
# # print(float(cur_json) * float(inputs[i][2]))
# # print(cur_json)

import requests
import json

cache = {}
currency_code = input().lower()
url = f"http://www.floatrates.com/daily/{currency_code}.json"
data = requests.get(url)
currency = json.loads(data.text)
if currency_code != 'usd':
    cache['usd'] = currency['usd']
if currency_code != 'eur':
    cache['eur'] = currency['eur']
while True:
    exch_currency = input().lower()
    if exch_currency != "":
        try:
            money = float(input())
            if exch_currency in cache:
                print(f"Checking the cache…\nOh! It is in the cache!\nYou received {round(money * currency[exch_currency]['rate'], 2)} {exch_currency.upper()}")
            else:
                url = f"http://www.floatrates.com/daily/{currency_code}.json"
                data = requests.get(url)
                print(data)
                currency = json.loads(data.text)
                print(currency)
                currency['a'] = 1
                print(currency)
                cache[exch_currency] = currency[exch_currency]

                print(f"Checking the cache…\nSorry, but it is not in the cache!\nYou received {round(money * currency[exch_currency]['rate'], 2)} {exch_currency.upper()}")
        except ValueError:
            break
    else:
        break