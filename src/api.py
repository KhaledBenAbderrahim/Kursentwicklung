from datetime import datetime, timedelta , date
from pprint import pprint

import requests

def get_rates(currencies, days):
    end_date = date.today()
    start_date = end_date - timedelta(days=days)

    symbols = ','.join(currencies)
    requete = f"https://api.exchangerate.host/timeseries?start_date={start_date}&end_date={end_date}&symbols={symbols}"
    r = requests.get(requete)
    if not r and not r.json():
        return False, False

    api_rates = r.json().get("rates")
    all_rates = {currency:[] for currency in currencies}
    all_days = sorted(api_rates.keys())
    for each_day in all_days:
        [all_rates[currency].append(rate) for currency,rate in api_rates[each_day].items()]


    return all_days, all_rates

if __name__ == '__main__':
    days , rates = get_rates(currencies=["USD","CAD"],days=0)
    pprint(days)
    pprint(rates)