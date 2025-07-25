import pandas as pd
import os

PRODUCTS_CSV = "data/products.csv"
ORDERS_CSV = "data/orders.csv"

def load_context():
    context = ""

    # Load product data
    if os.path.exists(PRODUCTS_CSV):
        df_products = pd.read_csv(PRODUCTS_CSV)
        product_context = "\n".join(df_products.astype(str).apply(" - ".join, axis=1))
        context += f"Product Data:\n{product_context}\n\n"

    # Load order data
    if os.path.exists(ORDERS_CSV):
        df_orders = pd.read_csv(ORDERS_CSV)
        order_context = "\n".join(df_orders.astype(str).apply(" - ".join, axis=1))
        context += f"Order Data:\n{order_context}\n"

    return context

def build_prompt(user_query):
    context = load_context()
    return f"Context:\n{context}\n\nUser Query:\n{user_query}\n\nAnswer:"
