# Dictionary for saving contacts
contacts = {}

# Decorator for handling user input error
def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Invalid command format"
    return wrapper

# Function for displaying a list of all contacts
def show_all_contacts():
    if not contacts:
        return "No contacts found"
    else:
        result = ""
        for name, phone in contacts.items():
            result += f"{name}: {phone}\n"
        return result

# Function to add a new contact
@input_error
def add_contact(input_str):
    _, name, phone = input_str.split()
    contacts[name] = phone
    return f"Added {name}: {phone}"

# Function for changing the phone number of an existing contact
@input_error
def change_phone(input_str):
    _, name, phone = input_str.split()
    contacts[name] = phone
    return f"Changed phone for {name} to {phone}"

# Function for outputting the phone number of a contact
@input_error
def get_phone(input_str):
    _, name = input_str.split()
    if name in contacts:
        return f"Phone for {name}: {contacts[name]}"
    else:
        return f"Contact {name} not found"

# The main function for processing user commands
def main():

    while True:
        user_input = input().lower()

        if user_input == "good bye" or user_input == "close" or user_input == "exit":
            print("Good bye!")
            break
        elif user_input == "hello":
            print("How can I help you?")
        elif user_input == "show all":
            print(show_all_contacts())
        elif user_input.startswith("add"):
            print(add_contact(user_input))
        elif user_input.startswith("change"):
            print(change_phone(user_input))
        elif user_input.startswith("phone"):
            print(get_phone(user_input))
        else:
            print("Invalid command. Try again.")

if __name__ == "__main__":
    main()