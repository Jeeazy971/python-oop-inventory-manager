# Python OOP Inventory Manager

A learning project for **solid Python OOP fundamentals**, built progressively through an inventory manager.

## Concepts covered

- Classes, objects, `__init__`, `self`
- Instance and class attributes
- Instance methods
- Encapsulation with `_` convention
- `@property` and setters
- `dataclass`
- Composition
- Simple inheritance and `super()`
- `__str__` / `__repr__`
- Simple polymorphism
- When to avoid OOP

## Project structure

```text
python-oop-inventory-manager/
├── notes/                          # Learning notes per step
├── src/
│   └── inventory_manager/
│       ├── __init__.py
│       ├── product.py              # Product with @property, validation, from_dict/to_dict
│       ├── product_variants.py     # PerishableProduct, BulkProduct (inheritance)
│       ├── supplier.py             # Supplier
│       ├── category.py             # Category
│       ├── stock_entry.py          # StockEntry (composition: Product + Supplier)
│       ├── cart_item.py            # CartItem
│       ├── inventory.py            # Inventory (list of dicts)
│       ├── catalog.py              # Catalog (polymorphism demo)
│       ├── models.py               # Address, InventoryConfig (dataclasses)
│       └── store.py                # Store — mini-project entry point
├── main.py                         # Demo entry point
├── pyproject.toml
├── README.md
└── README_FR.md
```

## Requirements

- Python >= 3.13
- No external dependencies

## Usage

```bash
# Clone the repository
git clone https://github.com/Jeeazy971/python-oop-inventory-manager.git
cd python-oop-inventory-manager

# Create and activate virtual environment
python -m venv .venv
source .venv/Scripts/activate  # Windows
# source .venv/bin/activate    # macOS/Linux

# Run the demo
PYTHONPATH=src python -m main
```

## Example output

```
Magasin "FoodKeep" — 3 produit(s) — 2 fournisseur(s) — valeur : 104.40€
Store(name='FoodKeep', products=3, suppliers=2)
Valeur totale : 104.40€
Fournisseurs : 2
[✓] Lait — 10 unités — 12.00€
None
1 produit(s) en stock bas :
 — Yaourt — 3 unités à 0.80€
```

## Module overview

| Module | Class | Role |
|---|---|---|
| `product.py` | `Product` | Core product entity with validation and properties |
| `product_variants.py` | `PerishableProduct` | Product with expiry date (inheritance) |
| `product_variants.py` | `BulkProduct` | Product with minimum order qty (inheritance) |
| `supplier.py` | `Supplier` | Supplier entity |
| `category.py` | `Category` | Product category with description |
| `stock_entry.py` | `StockEntry` | Stock reception (composition) |
| `cart_item.py` | `CartItem` | Shopping cart line item |
| `inventory.py` | `Inventory` | Named inventory of items |
| `catalog.py` | `Catalog` | Product catalog (polymorphism) |
| `models.py` | `Address` | Delivery address (dataclass) |
| `models.py` | `InventoryConfig` | Inventory configuration (dataclass) |
| `store.py` | `Store` | Store aggregating products and suppliers |