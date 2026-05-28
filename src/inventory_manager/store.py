from inventory_manager.product import Product
from inventory_manager.supplier import Supplier


class Store:

    def __init__(self, name: str):
        self.name = name
        self.products: list[Product] = []
        self.suppliers: list[Supplier] = []

    def add_product(self, product):
        self.products.append(product)

    def add_supplier(self, supplier):
        self.suppliers.append(supplier)

    def get_product(self, name) -> None:
        for p in self.products:
            if p.name == name:
                return p
        return None

    def total_value(self) -> float:
        return sum(p.total_value for p in self.products)

    def low_stock_products(self) -> list:
        return [p for p in self.products if p.is_low_stock()]

    def supplier_count(self) -> int:
        return len(self.suppliers)

    def get_summary(self) -> str:
        return (f"Magasin \"{self.name}\""
                f" — {len(self.products)} produit(s) — {len(self.suppliers)} fournisseur(s)"
                f" — valeur : {self.total_value():.2f}€")

    def __str__(self) -> str:
        return self.get_summary()

    def __repr__(self) -> str:
        return f"Store(name={self.name!r}, products={len(self.products)}, suppliers={len(self.suppliers)})"
