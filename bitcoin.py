import sys
import requests

API_KEY = "b800ada9706d0a0a9bbef5f4e39827aabd8fecff1a6d0517d41bdfe2db64065c"
URL = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={API_KEY}"


def main():
    n = get_number_of_bitcoins()
    price = get_bitcoin_price()
    amount = n * price
    # Four decimal places, with a comma as thousands separator
    print(f"${amount:,.4f}")


def get_number_of_bitcoins():
    # The number of Bitcoins comes from the command line: python bitcoin.py 2.5
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    try:
        return float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")


def get_bitcoin_price():
    # Ask the API for the current price and read it from the JSON response
    try:
        response = requests.get(URL)
        response.raise_for_status()
        data = response.json()
        return float(data["data"]["priceUsd"])
    except requests.RequestException:
        sys.exit("Could not reach the CoinCap API")
    except (KeyError, ValueError):
        sys.exit("Unexpected response from the CoinCap API")


if __name__ == "__main__":
    main()
