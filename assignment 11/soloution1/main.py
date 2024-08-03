import os
from items import Item
from laptop import Laptop

def main():
    # Path to the CSV file
    csv_path = 'data/items.csv'
    
    # Load items from CSV
    items = Item.load_items_from_csv(csv_path)
    
    # Create Laptop objects for demonstration
    laptop1 = Laptop(name="Gaming Laptop", price=1500, quantity=2, gpu="NVIDIA RTX 3080", port_count=4)
    items.append(laptop1)

    # Print all items
    Item.all_items(items)
    print(laptop1)

if __name__ == "__main__":
    main()