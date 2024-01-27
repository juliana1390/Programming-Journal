from database import add_entry, view_entries

menu = """Please select one of the following options:
1) Add new entry for today.
2) View entries.
3) Exit.

Your selection: """
welcome = "Welcome to the programming diary!"

entries = [
    {"content": "Today I started learning programming.", "date": "01-01-2024"},
    {"content": "I created my first SQLite database!", "date": "02-01-2024"},
    {"content": "I finished writing my programming diary application.", "date": "03-01-2024"},
    {"content": "Today I'm going to continue learning programming!", "date": "04-01-2024"},
]

print(welcome)

while (user_input := input(menu)) != "3":
    if user_input == "1":
        add_entry()
    elif user_input == "2":
        view_entries()
    else:
        print("Invalid option, please try again!")

    
