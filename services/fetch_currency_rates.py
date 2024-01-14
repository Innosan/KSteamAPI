import requests

from models.CurrencyRates import CurrencyRates
from models.Error import Error

fixer_base_url = "http://data.fixer.io/api/latest"
params = {
    "access_key": "a415575dea8b23bc1a76f030b4415306",
    "format": "1",
    "symbols": "USD,KZT,RUB"
}


def fetch_currency_rates():
    try:
        response = requests.get(fixer_base_url, params=params)
    except:
        return {
            "status": False,
            "error": Error(400, "Currency request failure!")
        }

    currency_rates = response.json()

    # Get the RUB rate
    rub_rate = currency_rates['rates']['RUB']

    # Create a new dictionary for the rates based on RUB
    new_rates = {currency: rate / rub_rate for currency, rate in currency_rates['rates'].items()}

    # Update the API response
    currency_rates['base'] = 'RUB'
    currency_rates['rates'] = new_rates

    return {
        "status": True,
        "rates": CurrencyRates(
            date=currency_rates["date"],
            tenge=currency_rates["rates"]["KZT"],
            dollar=currency_rates["rates"]["USD"]
        )
    }
