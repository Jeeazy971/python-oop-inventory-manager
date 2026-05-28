# Python OOP Inventory Manager

Projet d'apprentissage dédié à la **programmation orientée objet en Python**, construit progressivement à travers un gestionnaire d'inventaire.

## Concepts couverts

- Classes, objets, `__init__`, `self`
- Attributs d'instance et de classe
- Méthodes d'instance
- Encapsulation avec la convention `_`
- `@property` et setters
- `dataclass`
- Composition
- Héritage simple et `super()`
- `__str__` / `__repr__`
- Polymorphisme simple
- Quand éviter la POO

## Structure du projet

```text
python-oop-inventory-manager/
├── notes/                          # Notes de cours par step
├── src/
│   └── inventory_manager/
│       ├── __init__.py
│       ├── product.py              # Product avec @property, validation, from_dict/to_dict
│       ├── product_variants.py     # PerishableProduct, BulkProduct (héritage)
│       ├── supplier.py             # Supplier
│       ├── category.py             # Category
│       ├── stock_entry.py          # StockEntry (composition : Product + Supplier)
│       ├── cart_item.py            # CartItem
│       ├── inventory.py            # Inventory (liste de dicts)
│       ├── catalog.py              # Catalog (démonstration du polymorphisme)
│       ├── models.py               # Address, InventoryConfig (dataclasses)
│       └── store.py                # Store — point d'entrée du mini-projet
├── main.py                         # Point d'entrée de démonstration
├── pyproject.toml
├── README.md
└── README_FR.md
```

## Prérequis

- Python >= 3.13
- Aucune dépendance externe

## Utilisation

```bash
# Cloner le dépôt
git clone https://github.com/Jeeazy971/python-oop-inventory-manager.git
cd python-oop-inventory-manager

# Créer et activer l'environnement virtuel
python -m venv .venv
source .venv/Scripts/activate  # Windows
# source .venv/bin/activate    # macOS/Linux

# Lancer la démonstration
PYTHONPATH=src python -m main
```

## Résultat attendu

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

## Vue d'ensemble des modules

| Module                | Classe              | Rôle                                                 |
| --------------------- | ------------------- | ---------------------------------------------------- |
| `product.py`          | `Product`           | Entité produit avec validation et propriétés         |
| `product_variants.py` | `PerishableProduct` | Produit avec date d'expiration (héritage)            |
| `product_variants.py` | `BulkProduct`       | Produit avec quantité minimum de commande (héritage) |
| `supplier.py`         | `Supplier`          | Entité fournisseur                                   |
| `category.py`         | `Category`          | Catégorie de produit avec description                |
| `stock_entry.py`      | `StockEntry`        | Réception de stock (composition)                     |
| `cart_item.py`        | `CartItem`          | Ligne de panier d'achat                              |
| `inventory.py`        | `Inventory`         | Inventaire nommé d'articles                          |
| `catalog.py`          | `Catalog`           | Catalogue produits (polymorphisme)                   |
| `models.py`           | `Address`           | Adresse de livraison (dataclass)                     |
| `models.py`           | `InventoryConfig`   | Configuration d'inventaire (dataclass)               |
| `store.py`            | `Store`             | Magasin agrégeant produits et fournisseurs           |
