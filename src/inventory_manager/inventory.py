class Inventory:

    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, item_name, qty, price):
        item = {
            "name": item_name,
            "qty": qty,
            "price": price
        }

        self.items.append(item)

    def total_value(self):
        total = 0

        for item in self.items:
            total += item["price"] * item["qty"]

        return total

    def is_empty(self):
        return len(self.items) == 0

    def count(self):
        return len(self.items)

    def get_summary(self):
        return (
            f'Inventaire "{self.name}" — vide'
            if self.is_empty()
            else f'Inventaire "{self.name}" — {self.count()} article(s) — valeur totale : {self.total_value():.2f}€'
        )
