from inventory_manager.product import Product


class PerishableProduct(Product):

    def __init__(self, name, qty, price, expiry_date: str):
        super().__init__(name, qty, price)
        self.expiry_date = expiry_date

    def is_expired(self, today: str) -> bool:
        return self.expiry_date < today

    def get_summary(self) -> str:
        base = super().get_summary()
        return f"{base} — expire le {self.expiry_date}"


class BulkProduct(Product):

    def __init__(self, name, qty, price, min_order_qty: int):
        if min_order_qty <= 0:
            raise ValueError("min_order_qty doit être > 0")
        super().__init__(name, qty, price)
        self.min_order_qty = min_order_qty

    def can_order(self, qty) -> bool:
        return qty >= self.min_order_qty
    
    def get_summary(self) -> str:
        base = super().get_summary()
        return f"{base} — commande min : {self.min_order_qty} unités"
