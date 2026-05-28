class Supplier:
    MAX_PRODUCTS = 50

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def get_contact_info(self) -> str:
        return f"Supplier: {self.name} | email: {self.email} | phone: {self.phone}"

    def update_email(self, new_email):
        self.email = new_email

    def is_valid(self) -> bool:
        return self.name.strip() != "" and "@" in self.email.strip().lower()

    def get_summary(self) -> str:
        return f"[{self.name}] {self.email} - max {self.MAX_PRODUCTS} produits"

    def __repr__(self) -> str:
        return f"Supplier(name={self.name!r}, email={self.email!r})"
