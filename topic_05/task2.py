import requests

response = requests.get(
    "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?json"
)

currencies = response.json()

amount = float(input("Enter the amount: "))
currency = input("Enter currency (EUR, USD, PLN): ").upper()

rate = None

for elem in currencies:
    if elem["cc"] == currency:
        rate = elem["rate"]
        break

if rate is not None:
    result = amount * rate
    print("Course:", rate, "uan")
    print("Amount in hvyvnias:", round(result, 2), "uan")
else:
    print("Currency not found!")