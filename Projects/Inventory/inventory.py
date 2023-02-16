# import the necessary modules
import csv
from tabulate import tabulate

# define the Shoe class
class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return f"{self.code}, {self.product}, {self.country}, {self.cost}, {self.quantity}"

# create an empty list to store the Shoe objects
shoe_list = []

# define the read_shoes_data function to read the data from the file
def read_shoes_data():
    try:
        with open("inventory.txt", "r") as f:
            reader = csv.reader(f)
            next(reader)  # skip the header row
            for row in reader:
                shoe = Shoe(row[0], row[1], row[2], float(row[3]), int(row[4]))
                shoe_list.append(shoe)
    except FileNotFoundError:
        print("The file 'inventory.txt' could not be found.")

# define the capture_shoes function to allow the user to add a new shoe to the inventory
def capture_shoes():
    country = input("Enter the country: ")
    code = input("Enter the code: ")
    product = input("Enter the product: ")
    cost = float(input("Enter the cost: "))
    quantity = int(input("Enter the quantity: "))
    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe)

# define the view_all function to print the details of all the shoes in the inventory
def view_all():
    rows = []
    for shoe in shoe_list:
        rows.append([shoe.code, shoe.product, shoe.country, shoe.cost, shoe.quantity])
    print(tabulate(rows, headers=["Code", "Product", "Country", "Cost", "Quantity"], tablefmt="grid"))

# define the re_stock function to restock the shoe with the lowest quantity
def re_stock():
    min_quantity = min(shoe.quantity for shoe in shoe_list)
    for shoe in shoe_list:
        if shoe.quantity == min_quantity:
            print(f"The shoe with the code {shoe.code} needs to be restocked.")
            add_quantity = input("Do you want to add more shoes to the inventory? (Y/N): ")
            if add_quantity.lower() == "y":
                new_quantity = int(input("Enter the quantity to be added: "))
                shoe.quantity += new_quantity
                with open("inventory.txt", "w") as f:
                    writer = csv.writer(f)
                    writer.writerow(["Country", "Code", "Product", "Cost", "Quantity"])
                    for shoe in shoe_list:
                        writer.writerow([shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity])
            break

# define the search_shoe function to search for a shoe by its code
def search_shoe():
    code = input("Enter the code of the shoe you want to search for: ")
    for shoe in shoe_list:
        if shoe.code == code:
            print(shoe)
            break
    else:
        print(f"No shoe with the code {code} was found.")

# define the value_per_item function to calculate the total value for each shoe
def value_per_item():
    rows = []
    for shoe in shoe_list:
        value = shoe.cost * shoe.quantity
        rows.append([shoe.code, shoe.product, value])
    print(tabulate(rows, headers=["Code", "Product", "Total Value"], tablefmt="grid"))


# define the highest_qty function to determine the shoe with the highest quantity
def highest_qty():
    max_quantity = max(shoe.quantity for shoe in shoe_list)
    for shoe in shoe_list:
        if shoe.quantity == max_quantity:
            print(f"The {shoe.product} with the code {shoe.code} is for sale with the highest quantity of {shoe.quantity}.")
            break

# define the main function to display the menu and handle user input
def main():
    read_shoes_data()
    while True:
        print("\nWelcome to the Shoe Inventory Management System!\n")
        print("Please select an option:")
        print("1. View all shoes")
        print("2. Search for a shoe")
        print("3. Add a new shoe to the inventory")
        print("4. Re-stock a shoe")
        print("5. Show shoe with highest quantity")
        print("6. Show the value of each shoe")
        print("7. Exit\n")

        choice = input("Enter your choice: ")
        if choice == "1":
            view_all()
        elif choice == "2":
            search_shoe()
        elif choice == "3":
            capture_shoes()
        elif choice == "4":
            re_stock()
        elif choice == "5":
            highest_qty()
        elif choice == "6":
            value_per_item()
        elif choice == "7":
            print("Thank you for using the Shoe Inventory Management System!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
