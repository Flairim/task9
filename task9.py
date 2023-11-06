contact_book = {}  # Словник для зберігання контактів

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

def add_contact(command):
    parts = command.split()
    name, phone = parts[1], parts[2]
    contact_book[name] = phone
    return f"Added {name} with phone {phone}"

def change_phone(command):
    parts = command.split()
    name, phone = parts[1], parts[2]
    if name in contact_book:
        contact_book[name] = phone
        return f"Changed {name}'s phone to {phone}"
    else:
        return f"Contact {name} not found"

def get_phone(command):
    name = command.split()[1]
    if name in contact_book:
        return f"{name}'s phone is {contact_book[name]}"
    else:
        return f"Contact {name} not found"

def show_all_contacts(command):
    if not contact_book:
        return "No contacts in the book"
    contacts = "\n".join([f"{name}: {phone}" for name, phone in contact_book.items()])
    return contacts

def main():
    print("Bot assistant. Type 'hello' to start.")
    while True:
        user_input = input().strip().lower()
        if user_input in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        elif user_input == "hello":
            print("How can I help you?")
        elif user_input.startswith("add "):
            result = add_contact(user_input)
            print(result)
        elif user_input.startswith("change "):
            result = change_phone(user_input)
            print(result)
        elif user_input.startswith("phone "):
            result = get_phone(user_input)
            print(result)
        elif user_input == "show all":
            result = show_all_contacts(user_input)
            print(result)
        else:
            print("Invalid command. Type 'hello' to start or 'exit' to close.")

if __name__ == "__main__":
    main()
