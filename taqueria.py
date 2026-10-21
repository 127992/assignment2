# Menu: each item (key) maps to its price in dollars (value)
MENU = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}


def main():
    total = 0.0
    while True:
        try:
            # Title case so the input matches the menu keys (case-insensitive)
            item = input("Item: ").title()
            total += MENU[item]
            print(f"Total: ${total:.2f}")
        except KeyError:
            # Item not on the menu: ignore it and ask again
            pass
        except EOFError:
            # User pressed Ctrl+D: end the order
            print()
            break


if __name__ == "__main__":
    main()
