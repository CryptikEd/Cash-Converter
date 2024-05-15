import requests

logo = r"""
   _____          _        _____                          _
  / ____|        | |      / ____|                        | |
 | |     __ _ ___| |__   | |     ___  _ ____   _____ _ __| |_ ___ _ __
 | |    / _` / __| '_ \  | |    / _ \| '_ \ \ / / _ \ '__| __/ _ \ '__|
 | |___| (_| \__ \ | | | | |___| (_) | | | \ V /  __/ |  | ||  __/ |
  \_____\__,_|___/_| |_|  \_____\___/|_| |_|\_/ \___|_|   \__\___|_|
"""
print(logo)

# Welcome message and instructions for the user.
print("Welcome to the currency converter made by CryptikEd.")
print("This converter can convert all of the world's currencies.")
print("Please enter the following information under.")


def my_cash_converter():
    while True:
        # Prompt user to input the amount and currencies.
        while True:
            amount_str = input("Enter the amount to convert: ")
            # Check if the input string contains only digits.
            if amount_str.isdigit():
                break

            else:
                print("Invalid input: Please enter a valid number.")

        from_currency = input(
            "Enter the currency to convert from (e.g., USD, EUR, GBP): "
        ).upper()
        to_currency = input(
            "Enter the currency to convert to (e.g., USD, EUR, GBP): "
        ).upper()

        try:
            # Convert amount input to integer.
            amount = int(amount_str)

            # API endpoint URL with the user-provided currencies.
            api_key = "668f299de2059972cf666f65"
            endpoint = (
                f"https://v6.exchangerate-api.com/v6/{api_key}"
                f"/pair/{from_currency}/{to_currency}"
            )
            # Fetch exchange rates from the customized API.
            response = requests.get(endpoint)
            data = response.json()

            # Check if the conversion is possible.
            if "error" in data:
                print(
                    f"Conversion from {from_currency} to {to_currency} "
                    f"is not supported."
                )
            else:
                # Extract conversion rate from the response.
                conversion_rate = data["conversion_rate"]

                # Performs conversion and gives the user the amount he inputs.
                converted_amount = amount * conversion_rate
                print(
                    (
                        f"{amount} {from_currency} is equal to "
                        f"{converted_amount:.2f} {to_currency}"
                    )
                )

        except ValueError:

            # Handle invalid input for the amount.
            print("Invalid input: The amount must be a valid number.")
        except Exception as e:
            # Handle other exceptions such as network errors.
            print(f"An error occurred: {e}")

        # Prompt the user if they want to perform another conversion.
        while True:
            choice = input(
                "Do you want to perform another conversion? (yes/no): "
            ).lower()

            if choice == "yes" or choice == "no":
                break
            else:
                print("Invalid input: Please enter 'yes' or 'no'.")

        # If the user choice is not yes, ends the program.
        if choice != "yes":
            break


# Call the function to start the currency converter
my_cash_converter()
