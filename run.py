import requests

def my_currency_converter():
     
    print("Welcome to the currency converter made by CryptikEd.")
    print("This converter can convert all of the world's currencies.")
    print("Please enter the following information:")

    amount_str = input("Enter the amount to convert: ")
    from_currency = input("Enter the currency to convert from (e.g., USD, EUR, GBP): ").upper()
    to_currency = input("Enter the currency to convert to (e.g., USD, EUR, GBP): ").upper()

    try:
        # amount = float(amount_str) leave until tuesday to work out conversion rate*amount code that will be implemented to give user the amount he inserted in other currency.
        
        api_key = "668f299de2059972cf666f65"
        endpoint = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{from_currency}/{to_currency}"

        # Fetch exchange rates from the customized API
        response = requests.get(endpoint)
        data = response.json()

        # Check if the conversion is possible
        if 'error' in data:
            print(f"Conversion from {from_currency} to {to_currency} is not supported.")
        else:
            # Performs the conversion but doesnt give the amount user inputs. To be checked.
            #converted_amount = data['result'] leave until resolved.
            #print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
            print(data)

    except ValueError:
        print("Invalid input: The amount must be a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to start the currency converter
my_currency_converter()

# Ap