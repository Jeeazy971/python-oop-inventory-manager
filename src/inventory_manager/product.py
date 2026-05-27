class Product:

    def __init__(self, name, qty, price):
        if name.strip() == "":
            raise ValueError("Le nom du produit ne peut pas être vide")

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
            "qty": self._qty,
            "price": self._price
        }

    @property
    def qty(self) -> int:
        return self._qty
    
    
    @qty.setter
    def qty(self, value: int):
        if value < 0:
            raise ValueError("qty ne peut pas être négatif")
        self._qty = value

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float):
        if value < 0:
            raise ValueError("price ne peut pas être négatif")
        self._price = value

    @property
    def total_value(self) -> float:
        return self._qty * self._price
    
    def is_low_stock(self, threesold=5) -> bool:
        return self._qty < threesold

    def get_summary(self) -> str:
        return (f"[⚠] {self.name} — {self._qty} unités — {self.total_value:.2f}€"
                if self.is_low_stock() else
                f"[✓] {self.name} — {self._qty} unités — {self.total_value:.2f}€")
