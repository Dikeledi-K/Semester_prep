import random

Quotees = ["Abdullah Ibrahim", "Miriam Makeba", "Nelson Mandela", "Eleanor Roosevelt",
           "Anne Frank", "Alexander Graham Bell", "Thomas Edison", "Estee Lauder", "Maya Angelou", "Walt Disney"]

# Step 1: Update the function to choose a file based on user input
def ask_file_name(user_input):
    return user_input if user_input else "quotes.txt"

# Step 2: Correct the functionality to open the file and handle FileNotFoundError
def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            return file.read()  # Return the content of the file as a string
    except FileNotFoundError as e:
        print(f"FileNotFoundError successfully handled\n{e}")
        return ""

# Step 3: Randomly select a quotee from the Quotees list and return it
def select_random_quotee(Quotees):
    return random.choice(Quotees) if Quotees else ""

# Step 4: Correctly match a quote from the text file to the chosen quotee
def find_quote(random_quotee, quotes):
    for quote in quotes:
        if random_quotee in quote:
            return quote.strip()
    return "Quote/quotee does not exist."

# Step 5: Correctly print out the final results to pass the unit tests
def final_output(quote, quotee):
    if quote != "Quote/quotee does not exist.":
        quote_parts = quote.split("~")
        print("Quote found in file:")
        print(f"{quotee}: {quote_parts[1].strip()}")
    else:
        print(quote)

if __name__ == "__main__":
    """
     You can leave this code as is, and only implement the above steps.
     """
    user_input = input("Desired file? [leave empty to use quotes.txt] :")
    quotes_file = ask_file_name(user_input)
    print(repr(str(quotes_file)) + ': is your chosen file.\n')

    quotes = read_file(quotes_file).split("\n\n")  # Split content by double newlines
    random_quotee = select_random_quotee(Quotees)
    
    if random_quotee == "":
        print('Empty list.\n')
    else:
        print(f"{random_quotee} has randomly been chosen.\n")

    true_quote = find_quote(random_quotee, quotes)

    if true_quote == "Quote/quotee does not exist.":
        print(f"{random_quotee} is not present in the file\n")
    else:
        print(f"{random_quotee} is present in the file\n")
        final_output(true_quote, random_quotee)
