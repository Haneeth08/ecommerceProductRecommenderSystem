# main.py
from fastapi import FastAPI, Query
from typing import List

app = FastAPI()

# Sample Data
products = [
    {"product_id": 1, "product_name": "Laptop"},
    {"product_id": 2, "product_name": "Headphones"},
    {"product_id": 3, "product_name": "Smartphone"},
]

interactions = [
    {"user_id": "user1", "product_id": 1, "action": "view"},
    {"user_id": "user1", "product_id": 3, "action": "purchase"},
]

def recommend_products(user_id):
    # Basic logic: recommend products not interacted with
    user_products = {i["product_id"] for i in interactions if i["user_id"] == user_id}
    return [p for p in products if p["product_id"] not in user_products]

def llm_explanation(user_id, product):
    # Placeholder for LLM-powered explanation
    return f"Recommended because you have shown interest in similar products, {product['product_name']} suits your preferences."

@app.get("/recommendations")
def get_recommendations(user_id: str = Query(...)):
    recs = recommend_products(user_id)
    result = []
    for product in recs:
        result.append({
            "product_id": product["product_id"],
            "product_name": product["product_name"],
            "explanation": llm_explanation(user_id, product)
        })
    return result
