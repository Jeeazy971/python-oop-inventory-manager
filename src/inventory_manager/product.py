class Product:

    def __init__(self, name, qty, price):
        if name.strip() == "":
            raise ValueError("Le nom du produit ne peut pas être vide")
        if qty < 0:
            raise ValueError("La quantité du produit ne peut pas être < 0")
        if price < 0:
            raise ValueError("Le prix ne peut pas être < 0")

        self.name = name
        self.qty = qty
        self.price = price

    @classmethod
    def from_dict(cls, data: dict) -> "Product":
        return cls(
            name=data["name"],
            qty=data.get("qty", 0),
            price=data.get("price", 0.0)
        )

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "qty": self.qty,
            "price": self.price
        }

    def total_value(self):
        return self.qty * self.price

    def is_low_stock(self, threesold=5):
        return self.qty < threesold

    def get_summary(self):
        return (f"[⚠] {self.name} — {self.qty} unités — {self.total_value():.2f}€"
                if self.is_low_stock() else
                f"[✓] {self.name} — {self.qty} unités — {self.total_value():.2f}€")
