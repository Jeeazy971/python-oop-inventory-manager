class Supplier:
    MAX_PRODUCTS = 50

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def get_contact_info(self):
        return f"Supplier: {self.name} | email: {self.email} | phone: {self.phone}"

    def update_email(self, new_email):
        self.email = new_email

    def is_valid(self):
        return self.name.strip() != "" and "@" in self.email.strip().lower()

    def get_summary(self):
        return f"[{self.name}] {self.email} - max {self.MAX_PRODUCTS} produits"
