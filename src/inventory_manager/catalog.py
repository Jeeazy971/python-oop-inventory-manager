class Catalog:

    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

    def print_all(self):
        for p in self.products:
            print(p.get_summary())

    def total_value(self) -> float:
        return sum(p.total_value for p in self.products)

    def low_stock_items(self) -> list:
        return [p for p in self.products if p.is_low_stock()]

    def get_summary(self) -> str:
        return f"Catalogue — {len(self.products)} produit(s) — valeur totale : {self.total_value():.2f}€"
