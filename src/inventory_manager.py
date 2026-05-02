# Inventory Manager

class InventoryManager:
    def __init__(self, master_stock, live_inventory):
        self.master_stock = master_stock
        self.live_inventory = live_inventory

    def load_master_stock(self, stock_data):
        self.master_stock = stock_data

    def compare_inventory(self):
        stock_gaps = {}
        for item, quantity in self.master_stock.items():
            if item in self.live_inventory:
                live_quantity = self.live_inventory[item]
                if live_quantity < quantity:
                    stock_gaps[item] = quantity - live_quantity
            else:
                stock_gaps[item] = quantity
        return stock_gaps

    def calculate_stock_gaps(self):
        return self.compare_inventory()