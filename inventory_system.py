"""
Inventory management system.
This module provides functions to manage stock items.
"""
import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Global variable
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """Add quantity to inventory item."""
    if logs is None:
        logs = []
    # Type validation
    if not isinstance(item, str) or not item.strip():
        logging.error("Invalid item name: %s", item)
        return logs
    if not isinstance(qty, int) or qty < 0:
        logging.error("Invalid quantity: %s", qty)
        return logs
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")
    return logs


def remove_item(item, qty):
    """Remove quantity from inventory item."""
    if item not in stock_data:
        logging.warning("Item '%s' not found", item)
        return False
    if stock_data[item] < qty:
        logging.warning("Not enough %s. Have: %d, Need: %d", item, stock_data[item], qty)
        return False
    stock_data[item] -= qty
    if stock_data[item] <= 0:
        del stock_data[item]
    return True


def get_qty(item):
    """Get quantity of an item."""
    if item in stock_data:
        return stock_data[item]
    return None


def load_data(file="inventory.json"):
    """Load inventory data from JSON file."""
    global stock_data  # pylint: disable=global-statement
    try:
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, dict):
                stock_data = data
            else:
                logging.error("Invalid data format")
    except FileNotFoundError:
        logging.warning("File %s not found", file)
    except json.JSONDecodeError:
        logging.error("Invalid JSON format")


def save_data(file="inventory.json"):
    """Save inventory data to JSON file."""
    try:
        with open(file, "r", encoding="utf-8") as f:
            json.dump(stock_data, f, indent=2)
    except (IOError, OSError) as e:
        logging.error("Error saving: %s", e)


def print_data():
    """Print formatted inventory report."""
    print("Items Report")
    for i in stock_data:
        print(i, " -> ", stock_data[i])


def check_low_items(threshold=5):
    """Check for items below threshold quantity."""
    if threshold < 0:
        logging.warning("Threshold cannot be negative")
        threshold = 0
    result = []
    for i in stock_data:
        if stock_data[i] < threshold:
            result.append(i)
    return result


def main():
    """Main function to run inventory operations."""
    add_item("apple", 10)
    add_item("banana", -2)
    add_item(123, "ten")  # invalid types, no check
    remove_item("apple", 3)
    remove_item("orange", 1)
    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())
    save_data()
    load_data()
    print_data()


if __name__ == "__main__":
    main()
