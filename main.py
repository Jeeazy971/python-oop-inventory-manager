"""
Python OOP Inventory Manager — Demo entry point
Run: PYTHONPATH=src python -m main
"""

from inventory_manager.product import Product
from inventory_manager.product_variants import PerishableProduct, BulkProduct
from inventory_manager.supplier import Supplier
from inventory_manager.store import Store


def main():
    # ── Création du magasin ───────────────────
    store = Store("FoodKeep")

    # Fournisseurs
    store.add_supplier(
        Supplier("Carrefour", "contact@carrefour.fr", "0612345678"))
    store.add_supplier(Supplier("Metro", "pro@metro.fr", "0698765432"))

    # Produits — types variés pour démontrer le polymorphisme
    store.add_product(Product("Lait", 10, 1.20))
    store.add_product(PerishableProduct("Yaourt", 3, 0.80, "2025-06-01"))
    store.add_product(BulkProduct("Farine", 100, 0.90, 10))

    # ── Résumé du magasin ─────────────────────
    print("=== Magasin ===")
    print(store)
    print(repr(store))
    print(f"Valeur totale  : {store.total_value():.2f}€")
    print(f"Fournisseurs   : {store.supplier_count()}")

    # ── Recherche de produit ───────────────────
    print("\n=== Recherche ===")
    p = store.get_product("Lait")
    if p:
        print(p.get_summary())

    p_absent = store.get_product("Beurre")
    print(p_absent)  # → None

    # ── Produits en stock bas ─────────────────
    print("\n=== Stock bas ===")
    low = store.low_stock_products()
    print(f"{len(low)} produit(s) en stock bas :")
    for p in low:
        print(f"  — {p}")


if __name__ == "__main__":
    main()
