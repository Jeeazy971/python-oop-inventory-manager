class StockEntry:

    def __init__(self, product_name, quantity, unit_price, supplier_name="Inconnu"):
        if not product_name or not product_name.strip():
            raise ValueError("Le nom du produit ne peut pas être vide")
        if quantity <= 0:
            raise ValueError(f"La quantité doit être > 0, reçu : {quantity}")
        if unit_price <= 0:
            raise ValueError(
                f"Le prix unitaire doit être > 0, reçu : {unit_price}")

        self.product_name = product_name
        self.quantity = quantity
        self.unit_price = unit_price
        self.supplier_name = supplier_name
        self.total_cost = round(quantity * unit_price, 2)

    def get_receipt(self):
        return f"Réception — {self.product_name} (x{self.quantity}) @ {self.unit_price:.2f}€/u — Total : {self.total_cost:.2f}€ [{self.supplier_name}]"

    def is_large_order(self, threshold):
        return self.total_cost > threshold
