import requests

def my_currency_converter():
    while True:
        # find logo and input
     
         #Welcome message and instructions for the user
         print("Welcome to the currency converter made by CryptikEd.")
         print("This converter can convert all of the world's currencies.")
         print("Please enter the following information under.")
         
         # Prompt user to input the amount and currencies
         while True:
             amount_str = input("Enter the amount to convert: ")
             if amount_str.isdigit():
                 break

             else:
                print("Invalid input: Please enter a valid number.")
         
         from_currency = input("Enter the currency to convert from (e.g., USD, EUR, GBP): ").upper()
         to_currency = input("Enter the currency to convert to (e.g., USD, EUR, GBP): ").upper()

         try:
            # Convert amount input to integer
            amount = int (amount_str) 

            # API endpoint URL with the user-provided currencies
            api_key = "668f299de2059972cf666f65"
            endpoint = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{from_currency}/{to_currency}"

             # Fetch exchange rates from the customized API
            response = requests.get(endpoint)
            data = response.json()

            # Check if the conversion is possible
            if 'error' in data:
                 print(f"Conversion from {from_currency} to {to_currency} is not supported.")
            else:
                 # Extract conversion rate from the response
                conversion_rate = data['conversion_rate']

                # Performs the conversion and gives the user the amount he inputs.
                converted_amount = amount * conversion_rate 
                print((f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}"))
        
        

         except ValueError:
             # Handle invalid input for the amount
             print("Invalid input: The amount must be a valid number.")
         except Exception as e:
             # Handle other exceptions such as network errors
             print(f"An error occurred: {e}")
        
         choice = input("Do you want to perform another conversion? (yes/no): ").lower()
         if choice != 'yes':
             break

# Call the function to start the currency converter
my_currency_converter()