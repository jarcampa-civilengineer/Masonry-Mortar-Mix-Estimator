def ask_positive(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print("Enter a number greater than zero.")
        except ValueError:
            print("Please enter a valid number.")

def ask_choice(prompt, choices):
    while True:
        value = input(prompt).strip().upper()
        if value in choices:
            return choices[value]
        print("Invalid selection. Options:", ", ".join(choices.keys()))
