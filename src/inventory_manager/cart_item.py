class CartItem:

    def __init__(self, product_name, unit_price, quantity=1):
        if unit_price <= 0:
            raise ValueError("Le prix unitaire doit être > 0")
        if quantity <= 0:
            raise ValueError("La quantité doit être > 0")

        self.product_name = product_name
        self.unit_price = unit_price
        self.quantity = quantity

    def subtotal(self):
        return self.unit_price * self.quantity

    def apply_discount(self, percent):
        self.unit_price = round(
            self.unit_price - self.unit_price * percent / 100, 2)

    def increase_qty(self, amount):
        self.quantity += amount

    def get_label(self):
        return f"{self.product_name} x {self.quantity} = {self.subtotal():.2f}€"
