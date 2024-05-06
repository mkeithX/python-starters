import os
import sys
import requests
import datetime

def convert_currency(amount, from_currency, to_currency):

    url = f'https://api.exchangerate-api.com/v4/latest/{from_currency}'

    response = requests.get(url)
    rates = response.json()['rates']

    converted_amount = amount * rates[to_currency]

    return converted_amount


def user_input():
    amount = float(input("Enter amount: "))
    from_currency = input("Convert FROM (e.g. USD): ").upper()
    to_currency = input("Convert TO (e.g. PHP): ").upper()
    today = datetime.date.today()
    result = convert_currency(amount, from_currency, to_currency)
    print('\n')
    print(f"As of {today}:")
    print(f"{from_currency} {amount:.2f} is equivalent to {to_currency} {result:.2f}")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    app_name = 'Currency Converter'
    print(f'{"-" * 48}')
    print(f'{" " * 12}{app_name}{" " * 12}')
    print(f'{"-" * 48}')
    user_input()
    
    while True:
        response = input('\nDo you want to continue? (Y/N) ')
        if response == 'y' or response == 'Y':
            main()
        elif response == 'n' or response == 'N':
            print('\nThank you and have a great day.\n')
            sys.exit()
        else:
            print('\nError: Please select y or n.\n')
            continue

if __name__ == '__main__':
    main()