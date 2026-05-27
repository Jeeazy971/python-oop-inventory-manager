class StockEntry:

    def __init__(self, product: "Product", supplier: "Supplier", quantity: int):
        if quantity <= 0:
            raise ValueError("La quantité doit être > 0")

        self.product = product
        self.supplier = supplier
        self.quantity = quantity
        self.total_cost = round(product.price * quantity, 2)

    def get_receipt(self) -> str:
        return (
            f"Réception — {self.product.name} (x{self.quantity})"
            f" @ {self.product.price:.2f}€/u"
            f" Total : {self.total_cost:.2f}€ [{self.supplier.name}]"
        )

    def is_large_order(self, threshold) -> bool:
        return self.total_cost > threshold
