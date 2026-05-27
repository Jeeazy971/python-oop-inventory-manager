from dataclasses import dataclass


@dataclass
class Address:
    street: str
    city: str
    zipcode: str
    country: str = "France"

    def full_address(self):
        return f"{self.street}, {self.zipcode} {self.city}, {self.country}"


@dataclass
class InventoryConfig:
    max_items: int = 1000
    low_stock_threshold: int = 5
    currency: str = "EUR"

    def __post_init__(self):
        if self.low_stock_threshold >= self.max_items:
            raise ValueError("low_stock_threshold doit être < max_items")

    def is_low_stock(self, qty):
        return qty < self.low_stock_threshold
