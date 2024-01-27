from database import add_entry, get_entries

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
        entry_content = input("What have you learned today? ")
        entry_date = input("Enter the date: ")

        add_entry(entry_content, entry_date)
    elif user_input == "2":
        entries = get_entries()

        for entry in entries:
            print(f"{entry['date']}\n{entry['content']}\n\n")
    else:
        print("Invalid option, please try again!")

    
